#!/usr/bin/env python3
import os
import csv
import re
import random
import sys
import ssl

from connector import IRC

dirname = os.path.dirname(__file__)

server = os.getenv('IRC_SERVER', None)
port = int(os.getenv('IRC_PORT', '6697'))
channel = os.getenv('IRC_CHANNEL', '#random')
nick = os.getenv('IRC_NICK', 'emoji-bot')
user = os.getenv('IRC_USER', 'emoji-bot')
gecos = os.getenv('IRC_GECOS', 'Emoji Bot v0.3.1 (github.com/AlexGustafsson/irc-emoji-bot)')

if server is None:
    print('Cannot start the bot without a given server')
    sys.exit()

emojis = None
with open(os.path.join(dirname, './emojis.csv'), 'r') as file:
    reader = csv.reader(file)
    emojis = {row[0]: row[1] for row in reader if row and row[0]}


def handle_emoji(possible_emojis):
    for possible_emoji in possible_emojis:
        if possible_emoji in emojis:
            irc.send(channel, emojis[possible_emoji])


def handle_help():
    command, emoji = random.sample(emojis.items(), 1)[0]
    irc.send(channel, 'I replace your emoji mentions with actual ASCII emojis. Example:')
    irc.send(channel, '{0} -> {1}'.format(command, emoji))
    irc.send(channel, 'You can also use the following commands:')
    irc.send(channel, '{0}: (bond) freeze, sucka!!! -> ┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿ freeze, sucka!!!'.format(nick))
    irc.send(channel, '{0}: help -> this help text'.format(nick))


def handle_emoji_with_text(body):
    # Remove the nick prompt and trim whiteline
    body = body[len(nick) + 1:].strip()
    emoji_regex = re.compile("(\\([a-z0-9]+\\))")
    parts = emoji_regex.split(body)

    result = ''
    for part in parts:
        result += emojis[part] if part in emojis else part

    irc.send(channel, result)


def handle_message(message):
    sender, type, target, body = message
    if type == 'PRIVMSG':
        print(body)
        if body == '{0}: help'.format(nick):
            handle_help()
        elif re.match('^{0}:.*\\([a-z0-9]+\\).*'.format(nick), body) is not None:
            handle_emoji_with_text(body)
        else:
            possible_emojis = re.findall('(\\([a-z0-9]+\\))', body)
            handle_emoji(possible_emojis)


irc = IRC()

print('Bot: Connecting to {0}:{1} as {2} ({3})'.format(server, port, user, nick))
irc.connect(server, port, user, nick, gecos)
print('Bot: Connected to {0}'.format(server))

print('Bot: Joining channel {0}'.format(channel))
irc.join(channel)

print('Bot: Starting event loop')
while True:
    message = irc.retrieveMessage()
    handle_message(message)
