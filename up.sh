#!/usr/bin/env bash

# Please see the README for more information
docker run \
  --env IRC_SERVER='irc.example.org' \
  --env IRC_PORT='6697' \
  --env IRC_CHANNEL='#random' \
  --env IRC_NICK='emoji-bot' \
  --env IRC_USER='emoji-bot' \
  --env IRC_GECOS='Emoji Bot v0.3.0 (github.com/AlexGustafsson/irc-emoji-bot)' \
  --name irc-emoji-bot \
  --detach \
  --restart always \
  --cpus=0.5 \
  --memory=10MB \
  axgn/irc-emoji-bot
