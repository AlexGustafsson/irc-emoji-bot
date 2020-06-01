"""Easy to use module for connection to IRC."""

from __future__ import annotations

import logging
import textwrap
import threading
from logging import Logger
from queue import Queue
from socket import getdefaulttimeout
from threading import Event, Thread
from time import sleep
from typing import Generator, Optional, Set, Type

from irc.exception import IRCConnectionException, IRCException, IRCSocketClosedException, IRCSocketException
from irc.messages import IRCBaseMessage, IRCControlMessage, IRCMessage
from irc.socket import Socket


class IRC:  # pylint: disable=too-many-instance-attributes,too-many-arguments
    """IRC connector."""

    def __init__(
            self,
            server: str,
            port: int,
            user: str,
            nick: str,
            gecos: str = "",
            timeout: Optional[float] = getdefaulttimeout(),
            use_tls: bool = False,
            logger: Optional[Logger] = None
    ) -> None:
        self.__timeout: float = timeout or 1
        self.__logger = logging.getLogger(__name__) if logger is None else logger
        self.__socket = Socket(server, port, timeout, logger=self.__logger, use_tls=use_tls)
        self.__user = user
        self.__nick = nick
        self.__gecos = gecos

        # Create a thread and event handler for ingress messages
        self.__ingress_thread_should_run = Event()
        self.__ingress_thread = Thread(target=self.__handle_ingress_messages)
        self.__ingress_thread.daemon = True
        # Queue of parsed messages received from the server
        self.__ingress_messages: Queue[IRCBaseMessage] = Queue()  # pylint: disable=unsubscriptable-object

        # Create a thread and event handler for egress messages
        self.__egress_thread_should_run = Event()
        self.__egress_thread = Thread(target=self.__handle_egress_messages)
        self.__egress_thread.daemon = True
        # Queue of raw messages to send to the server
        self.__egress_messages: Queue[bytes] = Queue()  # pylint: disable=unsubscriptable-object

    @property
    def messages(self) -> Generator[IRCBaseMessage, None, None]:
        """A generator containing all received messages as they come."""
        while True:
            message = self.__ingress_messages.get()
            self.__ingress_messages.task_done()
            yield message

    def connect(self) -> None:
        """Connect to the server."""
        if self.__ingress_thread_should_run.is_set() or self.__egress_thread_should_run.is_set():
            raise IRCConnectionException("Already connected")

        # Connect the underlaying socket
        self.__socket.connect()

        # Logon
        self.send("User {0} {0} {0} :{1}\r\n".format(self.__user, self.__gecos))
        self.send("NICK {0}\r\n".format(self.__nick))

        self.__logger.info("Connected to server. Starting message threads")

        # Start the ingress thread
        self.__ingress_thread_should_run.set()
        self.__ingress_thread.start()

        # Start the egress thread
        self.__egress_thread_should_run.set()
        self.__egress_thread.start()

    def reconnect(self) -> None:
        """Reconnect to the server."""
        if not self.__ingress_thread_should_run.is_set() or not self.__egress_thread_should_run.is_set():
            raise IRCConnectionException("Not connected")

        # Connect the underlaying socket
        self.__socket.connect()

        # Logon
        self.send("User {0} {0} {0} :{1}\r\n".format(self.__user, self.__gecos))
        self.send("NICK {0}\r\n".format(self.__nick))

        self.__logger.info("Connected to server. Starting message threads")

    def disconnect(self) -> None:
        """Disconnect from the server."""
        # Tell the message threads to stop handling jobs
        self.__ingress_thread_should_run.clear()
        self.__egress_thread_should_run.clear()

        # Join the threads - waiting for them to complete before returning
        # from the disconnect call
        is_ingress_thread = threading.currentThread() is not self.__ingress_thread
        is_egress_thread = threading.currentThread() is not self.__egress_thread
        if not is_ingress_thread and not is_egress_thread:
            self.__ingress_thread.join()
            self.__egress_thread.join()

    def send(self, message: str) -> None:
        """Send a raw message to the server."""
        if len(message.encode()) > 512:
            raise IRCException("Message is too long. Cannot be longer than 512 bytes - was {}"
                               .format(len(message.encode())))

        self.__egress_messages.put(message.encode())

    def send_message(self, target: str, message: str) -> None:
        """Send a message."""
        self.__logger.debug("Sending message to %s", target)

        for line in textwrap.wrap(message, width=(512 - len(target) - 12)):
            self.send("PRIVMSG {} :{}\r\n".format(target, line))

    def send_notice(self, target: str, notice: str) -> None:
        """Send a notice."""
        self.__logger.debug("Sending notice to %s", target)

        for line in textwrap.wrap(notice, width=(512 - len(target) - 11)):
            self.send("NOTICE {} :{}\r\n".format(target, line))

    def join(self, channel: str) -> None:
        """Join a channel."""
        self.__logger.debug("Joining channel %s", channel)
        self.send("JOIN {}\r\n".format(channel))

    def __handle_ingress_messages(self) -> None:
        """Threaded ingress entrypoint of the IRC client."""
        # An increasing timeout
        timeout = self.__timeout

        # Run the connector's main loop for as long as it's not disconnected
        while self.__ingress_thread_should_run.is_set():
            try:
                raw_data = self.__socket.read_all()
            except IRCSocketClosedException:
                self.__logger.info("Socket has closed, trying to reconnect")
                try:
                    self.reconnect()
                except IRCException:
                    self.__logger.error("Unable to reconnect", exc_info=True)
                    self.__logger.debug("Trying to reconnect again in %ds", timeout)
                    sleep(timeout)
                    timeout += timeout
                continue

            # If there is no data, continously poll the socket for more data
            # and back off exponentially
            if raw_data is None:
                self.__logger.debug("No data available, waiting %ds", timeout)
                try:
                    self.__socket.wait_for_data(timeout)
                except IRCSocketException:
                    timeout += timeout
                continue
            timeout = self.__timeout

            lines = raw_data.decode().splitlines()
            self.__logger.debug("Server sent %d lines", len(lines))
            for line in lines:
                # Try to parse the line using all available message parsers
                parsers: Set[Type[IRCBaseMessage]] = {IRCControlMessage, IRCMessage}
                messages = [parser.parse(line) for parser in parsers]
                # Add each non-null message to the message queue
                parsed_messages = [message for message in messages if message is not None]

                if len(parsed_messages) == 0:
                    # Handle pinging internally - don't expose it as a message
                    if line.startswith("PING"):
                        self.__logger.debug("Got PING, responding with PONG")
                        self.send("PONG {}\r\n".format(line.split(" ")[1:]))
                    else:
                        self.__logger.debug("Unhandled message: <%s>", line)
                else:
                    # Add all parsed messages to the message queue
                    for parsed_message in parsed_messages:
                        self.__ingress_messages.put(parsed_message)
                    self.__logger.debug("Parsed %d messages and added them to the queue", len(parsed_messages))

    def __handle_egress_messages(self) -> None:
        """Threaded egress entrypoint of the IRC client."""
        while self.__egress_thread_should_run.is_set():
            message = self.__egress_messages.get()
            try:
                self.__socket.write(message)
                self.__egress_messages.task_done()
            except IRCSocketException:
                self.__logger.error("Unable to send message", exc_info=True)
