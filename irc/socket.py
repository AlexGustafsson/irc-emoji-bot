"""Module for abstracting low-level sockets."""

import logging
import socket
from logging import Logger
from select import select
from ssl import SSLError, SSLWantReadError, SSLWantWriteError, create_default_context
from typing import Optional

from irc.exception import IRCSocketClosedException, IRCSocketException


class Socket:
    """Socket."""

    def __init__(  # pylint: disable=too-many-arguments
            self,
            server: str,
            port: int,
            timeout: Optional[float] = socket.getdefaulttimeout(),
            use_tls: bool = True,
            logger: Optional[Logger] = None
    ) -> None:
        self.__server = server
        self.__port = port
        self.__timeout: float = timeout or 1
        self.__use_tls = use_tls
        self.__logger = logging.getLogger(__name__) if logger is None else logger
        self.__socket: socket.socket

    def __wait_for_read(self, raw_socket: socket.socket, timeout: float) -> None:
        """Wait for the socket to be readable."""
        self.__logger.debug("Waiting for socket to be readable")
        ready_to_read, _, _ = select([raw_socket], [], [], timeout)
        if raw_socket not in ready_to_read:
            raise IRCSocketException("Socket operation timed out")

    def __wait_for_write(self, raw_socket: socket.socket, timeout: float) -> None:
        """Wait for the socket to be writable."""
        self.__logger.debug("Waiting for socket to be writable")
        _, ready_to_write, _ = select([], [raw_socket], [], timeout)
        if raw_socket not in ready_to_write:
            raise IRCSocketException("Socket operation timed out")

    def write(self, data: bytes) -> None:
        """Write bytes to a socket."""
        data_to_send = data
        total_bytes = len(data_to_send)
        self.__logger.debug("Writing %d bytes", total_bytes)
        while len(data_to_send) > 0:
            try:
                sent_bytes = self.__socket.send(data_to_send)
                data_to_send = data_to_send[sent_bytes:]
                self.__logger.debug("Wrote %d bytes", sent_bytes)
            except SSLWantWriteError:
                # Waiting for socket to be writable before continuing
                try:
                    self.__wait_for_write(self.__socket, self.__timeout)
                except IRCSocketException:
                    break
            except BlockingIOError:
                # Waiting for socket to be writable before continuing
                try:
                    self.__wait_for_write(self.__socket, self.__timeout)
                except IRCSocketException:
                    break
            except IRCSocketException as exception:
                raise exception

        self.__logger.debug("Done writing. Wrote %d bytes", total_bytes)

    def read(self, bytes_to_read: int) -> Optional[bytes]:
        """Read at most bytes_to_read bytes from a socket. Use -1 to read all."""
        received_bytes = bytes()
        self.__logger.debug("Reading at most %d bytes", bytes_to_read)

        bytes_left = bytes_to_read
        while bytes_left != 0:
            try:
                received_part = self.__socket.recv(4096)
                self.__logger.debug("Read %d bytes", len(received_part))

                # Check if the server killed the connection
                if len(received_part) == 0:
                    raise IRCSocketClosedException("Server killed the connection")

                received_bytes += received_part
                bytes_left = bytes_left - len(received_part)
            except SSLWantReadError:
                # Waiting for socket to be readable before continuing
                # Use a much lower timeout here, since this may occur
                # at the end of a call, when no more data is available
                try:
                    self.__wait_for_read(self.__socket, 0.1)
                except IRCSocketException:
                    break
            except (ConnectionResetError, BrokenPipeError) as exception:
                raise IRCSocketClosedException("Lost connection to server") from exception
            except BlockingIOError:
                # Waiting for socket to be readable before continuing
                # Use a much lower timeout here, since this may occur
                # at the end of a call, when no more data is available
                try:
                    self.__wait_for_read(self.__socket, 0.1)
                except IRCSocketException:
                    break
            except IRCSocketException as exception:
                raise exception

        if len(received_bytes) == 0:
            self.__logger.debug("Read nothing")
            return None

        self.__logger.debug("Done reading. Read %d bytes", len(received_bytes))
        return received_bytes

    def read_all(self) -> Optional[bytes]:
        """Read all data available."""
        return self.read(-1)

    def __upgrade_socket(self, raw_socket: socket.socket) -> socket.socket:
        """Upgrade a socket for TLS."""
        self.__logger.debug("Upgrading socket for TLS")

        # Create a TLS context and wrap the raw socket
        tls_context = create_default_context()
        tls_socket = tls_context.wrap_socket(
            raw_socket,
            server_hostname=self.__server,
            do_handshake_on_connect=False
        )

        # Try to complete the TLS handshake
        while True:
            try:
                # Try to perform a TLS handshake
                self.__logger.debug("Trying to perform TLS handshake")
                tls_socket.do_handshake()
            except SSLWantReadError:
                self.__wait_for_read(tls_socket, self.__timeout)
                continue
            except SSLWantWriteError:
                # If the socket is not yet writable, wait for it to be so
                self.__wait_for_write(tls_socket, self.__timeout)
                continue
            except SSLError as exception:
                # Re-raise any other errors
                raise IRCSocketException("Failed to connect via TLS") from exception
            break

        return tls_socket

    def connect(self) -> None:
        """Connect to the server."""
        try:
            # Create a connection with the specified server, port and timeout
            self.__logger.debug("Creating socket for %s:%s", self.__server, self.__port)
            self.__socket = socket.create_connection((self.__server, self.__port), self.__timeout)
        except socket.gaierror as exception:
            raise IRCSocketException("No such server") from exception
        except socket.timeout as exception:
            raise IRCSocketException("Connection timed out") from exception
        except ConnectionRefusedError as exception:
            raise IRCSocketException("Connection refused") from exception

        # Make the socket non-blocking
        self.__socket.setblocking(False)

        # Upgrade the socket if wanted
        if self.__use_tls:
            self.__socket = self.__upgrade_socket(self.__socket)

        self.__logger.debug("Connected")

    def wait_for_data(self, timeout: float) -> None:
        """Wait for data to be available."""
        self.__wait_for_read(self.__socket, timeout)
