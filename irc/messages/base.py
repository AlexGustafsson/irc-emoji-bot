"""IRC base message."""

from typing import Optional


class IRCBaseMessage():
    """IRC message base class."""

    def __init__(self, raw_message: str) -> None:
        self.__raw_message = raw_message

    @property
    def raw_message(self) -> str:
        """The original raw message as received by the server."""
        return self.__raw_message

    @staticmethod
    def parse(line: str) -> Optional["IRCBaseMessage"]:
        """Parse a message."""
