"""IRC message types."""

__package__ = "irc.messages"

# Explicitly export classes, disable linting rule not in favor
# Flake 8 (F401), however, needs to be per-line
# pylint: disable=useless-import-alias

from irc.messages.base import IRCBaseMessage as IRCBaseMessage  # noqa: F401
from irc.messages.control import IRCControlMessage as IRCControlMessage  # noqa: F401
from irc.messages.control import IRCControlMessageType as IRCControlMessageType  # noqa: F401
from irc.messages.message import IRCMessage as IRCMessage  # noqa: F401
