import traceback

def inverse(x):
    return 1 / x

try:
    inverse(0)
except Exception:
    traceback.print_exc(file=open('badly.txt', 'w'))

print('Bye')

# 2. How does it work?
    # 1. inverse(0) attempts to calculate 1 / 0.
    # 2. Python raises a ZeroDivisionError.
    # 3. except Exception catches the exception.
    # 4. traceback.print_exc() prints the complete traceback into badly.txt.
    # 5. print('Bye') executes because the exception was caught.
# 3. What does traceback.print_exc() do?
    # It generates the standard Python error report, including:
    # - Traceback header: indicates that an exception occurred.
    # - File and line numbers: shows where the error happened.
    # - Function calls: shows the sequence of calls leading to the error.
    # - Exception type and message: identifies the error.
# The argument:
    # file=open('badly.txt', 'w')
# means that the traceback is written to badly.txt instead of being displayed in the console.
# 4. What is the output?
    # When running the script:  Bye
    # The file badly.txt contains something similar to:
    # Traceback (most recent call last):
    #   File ".../badly.py", line 7, in <module>
    #     inverse(0)
    #   File ".../badly.py", line 4, in inverse
    #     return 1 / x
    # ZeroDivisionError: division by zero
# 5. Important distinction
    # Without catching the exception	                                        With traceback.print_exc()
    # Python displays the traceback automatically for an uncaught exception.	You catch the exception and manually record its traceback.
    # Program normally terminates.	                                            Program can continue executing.
    # Error appears in the console by default.	                                Error can be written to a file.