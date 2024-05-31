import threading

class Authenticator:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Authenticator, cls).__new__(cls)
        return cls._instance

# Client Code
def main():
    instance1 = Authenticator()
    instance2 = Authenticator()
    print(instance1 is instance2)

if __name__ == "__main__":
    main()
