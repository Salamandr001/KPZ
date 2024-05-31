class SmartTextReader:
    def read_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                matrix = [list(line.strip()) for line in lines]
            return matrix
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
