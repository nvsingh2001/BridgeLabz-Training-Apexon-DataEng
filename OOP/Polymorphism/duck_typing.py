class FileLogger:
    def write(self, message):
        print(f"Writing to file: {message}")


class ConsoleLogger:
    def write(self, message):
        print(f"Writing to console: {message}")


def log_something(logger):
    logger.write("Hello, world!")


log_something(FileLogger())
log_something(ConsoleLogger())
