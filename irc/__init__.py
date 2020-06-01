"""An easy-to-use IRC connector package."""

__package__ = "irc"

# Explicitly export classes, disable linting rule not in favor
# Flake 8 (F401), however, needs to be per-line
# pylint: disable=useless-import-alias

from irc.irc import IRC as IRC  # noqa: F401
