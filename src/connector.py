import socket
import ssl
import threading
import time
import queue
import sys

class IRC:
    def __init__(self):
        self.sock = None
        self.thread = None
        self.shouldRun = None
        self.messages = queue.Queue()

    def connect(self, server, port, user, nick, gecos=''):
        print('IRC: connecting to server')
        ssl_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = ssl.wrap_socket(ssl_sock)
        self.sock.connect((server, port))
        self.sock.send(bytes('USER {0} {0} {0} :{1}\r\n'.format(user, gecos), 'UTF-8'))
        self.sock.send(bytes('NICK {0}\r\n'.format(nick), 'UTF-8'))

        self.shouldRun = threading.Event()
        self.shouldRun.set()
        self.thread = threading.Thread(target=self.run, args=([self.shouldRun]))
        self.thread.daemon = True
        self.thread.start()

    def disconnect(self):
        self.shouldRun.clear()
        self.thread.join()

    def join(self, channel):
        self.sock.send(bytes('JOIN {0}\r\n'.format(channel), 'UTF-8'))

    def pong(self, key):
        self.sock.send(bytes('PONG :{0}\r\n'.format(key), 'UTF-8'))

    def send(self, channel, message):
        self.sock.send(bytes('PRIVMSG {0} :{1}\r\n'.format(channel, message), 'UTF-8'))

    def read(self):
        message = self.sock.recv(1024).decode('UTF-8').strip('\r\n')

        return message

    def run(self, shouldRun):
        time.sleep(2)
        while shouldRun.is_set():
            message = self.read()

            sys.stdout.flush()

            #:alex!~alex@nas.home PRIVMSG #emoji-bot-test :Hello world!
            #:irc.blesstherains.africa 372 emoji-bot :-
            #:emoji-bot!~emoji-bot@nas.home QUIT :Ping timeout: 2m30s
            #PING emoji-bot

            if message.find('PING') == 0:
                key = message.split(' ')[1]
                self.pong(key)
            else:
                parts = message.split(' ')
                sender = parts[0].split('!')[0][1:]
                message_type = parts[1]
                target = parts[2]
                message = ' '.join(parts[3:])[1:]

                self.messages.put((sender, message_type, target, message))

    def retrieveMessage(self):
        message = self.messages.get()
        self.messages.task_done()

        return message
