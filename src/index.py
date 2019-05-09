#!/usr/bin/env python3
import time
import os
import csv
import re
import random
import sys

from connector import IRC

dirname = os.path.dirname(__file__)

server = os.getenv('SERVER', None)
port = os.getenv('PORT', 6697)
channel = os.getenv('CHANNEL', '#random')
nick = os.getenv('NICK', 'emoji-bot')
user = os.getenv('USER', 'emoji-bot')
gecos = os.getenv('GECOS', 'Emoji Bot v0.1 (github.com/AlexGustafsson/irc-emoji-bot)')

if server == None:
    print('Cannot start the bot without a given server')
    sys.exit()

emojis = None
with open(os.path.join(dirname, './emojis.csv'), 'r') as file:
    reader = csv.reader(file)
    emojis = {row[0]:row[1] for row in reader if row and row[0]}

def handle_emoji(possible_emojis):
    for possible_emoji in possible_emojis:
        if possible_emoji in emojis:
            irc.send(channel, emojis[possible_emoji])

def handle_help():
    command, emoji = random.sample(emojis.items(), 1)[0]
    irc.send(channel, 'I replace your emoji mentions with actual ASCII emojis. Example:')
    irc.send(channel, '{0} -> {1}'.format(command, emoji))

def handle_message(message):
    sender, type, target, body = message
    if type == 'PRIVMSG':
        print(body)
        if body == '{0}: help'.format(nick):
            handle_help()
        else:
            possible_emojis = re.findall('(\([a-z]+\))', body)
            handle_emoji(possible_emojis)


irc = IRC()

print('Bot: Connecting to IRC')
irc.connect(server, port, user, nick, gecos)

print('Bot: Joining channel')
irc.join(channel)

print('Bot: Starting event loop')
while True:
    message = irc.retrieveMessage()
    handle_message(message)
