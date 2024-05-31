from FileLoggerAdapter import FileLoggerAdapter

def main():
    file_logger = FileLoggerAdapter('logfile.txt')

    file_logger.log('This is a log message')
    file_logger.error('This is an error message')
    file_logger.warn('This is a warning message')

if __name__ == '__main__':
    main()
