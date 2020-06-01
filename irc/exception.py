"""IRC connector exceptions."""


class IRCException(Exception):
    """IRC Exception."""


class IRCSocketException(IRCException):
    """IRC Socket Exception."""


class IRCSocketClosedException(IRCSocketException):
    """IRC Socket Closed Exception."""


class IRCConnectionException(IRCException):
    """IRC Connection Exception."""
