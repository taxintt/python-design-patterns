
class Logger(object):
    def __init__(self, handler) -> None:
        self.handler = handler

    def log(self, message):
        self.handler.emit(message)

class FilteredLogger(Logger):
    def __init__(self, pattern, handler) -> None:
        self.pattern = pattern
        super().__init__(handler)

    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FileHandler:
    def __init__(self, file) -> None:
        self.file = file

    def emit(self, message):
        self.file.write(message + "\n")
        self.file.flush()

class SocketHandler:
    def __init__(self, sock) -> None:
        self.sock = sock

    def emit(self, message):
        self.sock.sendall((message + '\n').encode('ascii'))