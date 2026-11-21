
"A context manager that traces entry and exit of any with statement's block"
class TraceBlock:

    def message(self, arg):
        print('running ' + arg)

    def __enter__(self):
        print('[starting with block]')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('[exited normally]\n')
        else:
            print(f'[propagating exception: {exc_type}]')
            return False

if __name__ == '__main__':
    with TraceBlock() as action:
        action.message('test 1')
        print('reached')

    with TraceBlock() as action:
        action.message('test 2')
        raise TypeError
        print('not reached')

# 3. Understanding the methods
# __enter__()

# def __enter__(self):
#     print('[starting with block]')
#     return self

    # Runs when entering the with block.
    # Prints a starting message.
    # Returns self, so the object is assigned to action.

# __exit__()

# def __exit__(self, exc_type, exc_value, exc_tb):
#     if exc_type is None:
#         print('[exited normally]\n')
#     else:
#         print(f'[propagating exception: {exc_type}]')
#     return False
    # Runs when leaving the with block.
    # If exc_type is None, no exception occurred.
    # Otherwise, an exception occurred, and its type is displayed.
    # return False allows the exception to propagate outside the with statement.
# Returning False is explicit, but deleting the return statement has the same effect because
# Python functions return None by default, which is also false.

# 4. Program execution
# First with block:
# with TraceBlock() as action:
#     action.message('test 1')
#     print('reached')
# [starting with block]
# running test 1
# reached
# [exited normally]
#
# No exception occurs, so __exit__() receives None for all three arguments.
# Second with block:
# with TraceBlock() as action:
#     action.message('test 2')
#     raise TypeError
#     print('not reached')
# [starting with block]
# running test 2
# [propagating exception: <class 'TypeError'>]
# Traceback (most recent call last):
# TypeError
#
# Execution:
# 1. __enter__() runs.
# 2. action.message('test 2') executes.
# 3. raise TypeError raises an exception.
# 4. print('not reached') is skipped.
# 5. __exit__() runs and receives the exception details.
# 6. It returns False, so Python propagates the TypeError
