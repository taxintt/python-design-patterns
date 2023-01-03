import sys
import syslog

class Logger(object):
    def __init__(self, file) -> None:
        self.file = file

    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush()


class SocketLogger(Logger):
    def __init__(self, sock) -> None:
        self.sock = sock

    def log(self, message):
        self.sock.sendall((message + '\n').encode('ascii'))


class SocketLogger(Logger):
    def __init__(self, priority) -> None:
        self.priority = priority

    def log(self, message):
        syslog.syslog(self.priority, message)

