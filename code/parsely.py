from time import asctime

class FormatError(Exception):
    logfile = 'parser-errors.txt'

    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logerror(self):
        with open(self.logfile, 'a') as log:
            print(f'Error at: {self.file} #{self.line} [{asctime()}]', file=log)

def parser(file):
    # Parse a file here...
    raise FormatError(line=62, file=file)

if __name__ == '__main__':
    try:
        parser('code.py')
    except FormatError as exc:
        exc.logerror()

# How it works:
# - logfile specifies the file where errors are recorded.
# - __init__ stores the line number and filename in instance attributes.
# - logerror() writes the error details and current time to the log file.
# - 'a' opens the file in append mode, so new errors are added rather than replacing existing content.
# - except FormatError as exc provides access to the raised exception instance.
# - exc.logerror() calls the method belonging to that instance.

