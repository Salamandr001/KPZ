import re
from SmartTextReader import SmartTextReader

class SmartTextReaderLocker:
    def __init__(self, reader, pattern):
        self.reader = reader
        self.pattern = re.compile(pattern)

    def read_file(self, filepath):
        if self.pattern.match(filepath):
            print("Access denied!")
            return None
        else:
            return self.reader.read_file(filepath)
