from SmartTextReader import SmartTextReader
from SmartTextChecker import SmartTextChecker
from SmartTextReaderLocker import SmartTextReaderLocker

def main():
    reader = SmartTextReader()

    # Logging proxy
    checker = SmartTextChecker(reader)
    print("Using SmartTextChecker:")
    checker.read_file('example.txt')

    # Access restriction proxy
    locker = SmartTextReaderLocker(reader, r'^restricted.*\.txt$')
    print("\nUsing SmartTextReaderLocker:")
    locker.read_file('example.txt')  # Should work
    locker.read_file('restricted_file.txt')  # Should be denied

if __name__ == "__main__":
    main()
