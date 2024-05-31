class Logger:
    @staticmethod
    def log(message):
        print(f"\033[92m{message}\033[0m")  # Green text

    @staticmethod
    def error(message):
        print(f"\033[91m{message}\033[0m")  # Red text

    @staticmethod
    def warn(message):
        print(f"\033[93m{message}\033[0m")  # Yellow text
