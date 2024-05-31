from SmartTextReader import SmartTextReader

class SmartTextChecker:
    def __init__(self, reader):
        self.reader = reader

    def read_file(self, filepath):
        print(f"Opening file: {filepath}")
        matrix = self.reader.read_file(filepath)
        if matrix is not None:
            print("File read successfully.")
            print(f"Total lines: {len(matrix)}")
            total_chars = sum(len(line) for line in matrix)
            print(f"Total characters: {total_chars}")
        else:
            print("Failed to read the file.")
        return matrix
