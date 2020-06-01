"""IRC message."""

import re
from typing import Optional

from irc.messages.base import IRCBaseMessage

# Regex for matching the individual parts of an IRC message
private_message_regex = re.compile("^:([^!]+)!(.*?) (PRIVMSG|NOTICE) ([^ ]+) :(.*)")


class IRCMessage(IRCBaseMessage):
    """An IRC private message."""

    def __init__(  # pylint: disable=too-many-arguments
            self,
            raw_message: str,
            author: str,
            hostname: str,
            is_notice: bool,
            target: str,
            message: str
    ) -> None:
        super().__init__(raw_message)

        self.__author = author
        self.__hostname = hostname
        self.__is_notice = is_notice
        self.__target = target
        self.__message = message

    @property
    def author(self) -> str:
        """The author of the message."""
        return self.__author

    @property
    def hostname(self) -> str:
        """The hostname of the message's author."""
        return self.__hostname

    @property
    def is_notice(self) -> bool:
        """Whether or not the message is a NOTICE."""
        return self.__is_notice

    @property
    def target(self) -> str:
        """The target of the message."""
        return self.__target

    @property
    def message(self) -> str:
        """The message itself."""
        return self.__message

    def __str__(self) -> str:
        """String representation of the message."""
        if self.__is_notice:
            return "NOTICE {} : {}".format(self.__author, self.__message)
        return "PRIVMSG {} : {}".format(self.__author, self.__message)

    @staticmethod
    def parse(line: str) -> Optional["IRCMessage"]:
        """Parse a message."""
        match = private_message_regex.match(line)
        if not match:
            return None

        author, hostname, type, target, message = match.groups()
        is_notice = type == "NOTICE"
        return IRCMessage(line, author, hostname, is_notice, target, message)
