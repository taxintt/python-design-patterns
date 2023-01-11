import syslog

class FileLogger:
    def __init__(self, file) -> None:
        self.file = file

    def log(self, message) -> None:
        self.file.write(message + "\n")
        self.file.flush()

class SocketLogger:
    def __init__(self, sock) -> None:
        self.sock = sock

    def log(self, message) -> None:
        self.sock.sendall((message + '\n').encode('ascii'))


class SyslogLogger:
    def __init__(self, priority) -> None:
        self.priority = priority

    def log(self, message) -> None:
        syslog.syslog(self.priority, message)

class LogFilter:
    def __init__(self, pattern, logger) -> None:
        self.pattern = pattern
        self.logger = logger

    def log(self, message):
        if self.pattern in message:
            self.logger.log(message)