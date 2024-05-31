from Logger import Logger
from FileWriter import FileWriter

class FileLoggerAdapter(Logger):
    def __init__(self, filename):
        self.file_writer = FileWriter(filename)

    def log(self, message):
        self.file_writer.write_line(f"LOG: {message}")

    def error(self, message):
        self.file_writer.write_line(f"ERROR: {message}")

    def warn(self, message):
        self.file_writer.write_line(f"WARN: {message}")
