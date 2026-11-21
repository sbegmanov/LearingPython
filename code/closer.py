
class MyError(Exception): pass

def stuff(file):
     file.write('Hello?')       # May be delayed in file buffer
     raise MyError()            # <= Enable or disable me with a #

if __name__ == '__main__':
    file = open('temp.txt', 'w') # Open an output file (this can fail too)
    try:
        stuff(file)              # Raises exception
    finally:
        file.close()             # Always close file to flush output buffers
    print('Am I reached?')       # Continue here only if no exception

# How it works:
# 1. open() opens the file for writing.
# 2. stuff(file) writes 'Hello?' into the file buffer.
# 3. raise MyError() raises an exception.
# 4. Python executes finally and closes the file.
# 5. The exception propagates, so print() is never executed.