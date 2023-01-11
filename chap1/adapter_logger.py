from syslog import syslog

class Logger(object):
    def __init__(self, file) -> None:
        self.file = file

    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush()

class FilteredLogger(Logger):
    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)

    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FileLikeSocket:
    def __init__(self, sock) -> None:
        self.sock = sock

    def write(self, message_and_newline):
        self.sock.sendall = message_and_newline.encode('ascii')

    def flush(self):
        pass

class FileLikeSyslog():
    def __init__(self, priority) -> None:
        self.priority = priority
    
    def write(self, message_and_newline):
        message = message_and_newline.rstrip('\n')
        syslog.syslog(self.priority, message)

    def flush(self):
        pass