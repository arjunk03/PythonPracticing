DEBUG = "debug"
INFO = "info"
WARNING = "warning"
ERROR = "error"


class Logger:
    def __init__(self, name):
        print("Logger instantiated : ", name)

    def log(self, message):
        print("imagine that this logs the message :", message)


class __ConsoleLogger(Logger):
    def __init__(self, name):
        Logger.__init__(self, name)

    def log(self, message):
        print("Logging to the console", message)


class __FileLogger(Logger):
    def __init__(self, name):
        Logger.__init__(self, name)

    def log(self, message):
        print("Logging to the file", message)


CONSOLE_LOGGER = __ConsoleLogger("console")
FILE_LOGGER = __FileLogger("file")
