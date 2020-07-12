import csv
import logging
import random
import re
from argparse import ArgumentParser
from os import path

from irc import IRC
from irc.messages import IRCMessage


def main() -> None:
    """Main entrypoint of the bot."""
    # Configure the default logging format
    logging.basicConfig(
        format="[%(asctime)s] [%(levelname)-5s] %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Create an argument parser for parsing CLI arguments
    parser = ArgumentParser(description="An IRC bot providing ASCII emojis")

    # Add parameters for the server connection
    parser.add_argument("-s", "--server", required=True, type=str, help="The server to connect to")
    # Add optional parameters for the server connection
    parser.add_argument("-p", "--port", default=6697, type=int, help="The port to connect to")
    parser.add_argument("--use-tls", default=True, type=bool, help="Whether or not to use TLS")
    parser.add_argument("-t", "--timeout", default=300, type=float, help="Connection timeout in seconds")

    # Add optional parameters for authentication etc.
    parser.add_argument("-u", "--user", default="emoji-bot", help="Username to use when connecting to the IRC server")
    parser.add_argument("-n", "--nick", default="emoji-bot", help="Nick to use when connecting to the IRC server")
    parser.add_argument("-g", "--gecos", default="Emoji Bot v1.0.1 (github.com/AlexGustafsson/irc-emoji-bot)", help="Gecos to use when connecting to the IRC server")
    parser.add_argument("-c", "--channel", required=True, action='append', help="Channel to join. May be used more than once")

    # Parse the arguments
    options = parser.parse_args()

    # Read emojis from disk
    emojis = None
    with open(path.join(path.dirname(__file__), "./emojis.csv"), "r") as file:
        reader = csv.reader(file)
        emojis = {row[0]: row[1] for row in reader if row and row[0]}

    # Create an IRC connection
    irc = IRC(
        options.server,
        options.port,
        options.user,
        options.nick,
        timeout=options.timeout,
        use_tls=options.use_tls
    )

    irc.connect()

    # Connect to specified channels
    for channel in options.channel:
        irc.join(channel)

    # Handle all messages
    for message in irc.messages:
        if not isinstance(message, IRCMessage):
            continue

        target = message.author if message.target == options.nick else message.target

        if message.message == "{}: help".format(options.nick):
            command = random.sample(list(emojis), 1)[0]
            irc.send_message(target, "I replace your emoji mentions with actual ASCII emojis. Example:")
            irc.send_message(target, "{} -> {}".format(command, emojis[command]))
            irc.send_message(target, "You can also use the following commands:")
            irc.send_message(target, "{}: (bond) freeze, sucka!!! -> ┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿ freeze, sucka!!!".format(options.nick))
            irc.send_message(target, "{}: help -> this help text".format(options.nick))
        elif re.match(r"^{}:.*\([a-z0-9]+\).*".format(options.nick), message.message) is not None:
            # Remove the nick prompt and trim whiteline
            body = message.message[len(options.nick) + 1:].strip()
            emoji_regex = re.compile(r"(\([a-z0-9]+\))")
            parts = emoji_regex.split(body)

            result = ""
            for part in parts:
                result += emojis[part] if part in emojis else part

            irc.send_message(target, result)
        else:
            possible_emojis = re.findall(r"(\([a-z0-9]+\))", message.message)
            for possible_emoji in possible_emojis:
                if possible_emoji in emojis:
                    irc.send_message(target, emojis[possible_emoji])


if __name__ == "__main__":
    main()
