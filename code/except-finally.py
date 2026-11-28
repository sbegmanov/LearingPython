
def raise1(): raise IndexError
def noraise(): return
def raise2(): raise SyntaxError

for func in (raise1, noraise, raise2):
    print(f'<{func.__name__}>')
    try:
        try:
            func()
        except IndexError:
            print('caught IndexError')
    finally:
        print('finally run')
print('...')

# How it works:
    # The loop calls each function and executes the nested exception handlers.
# Case 1: raise1()
    # - Raises IndexError.
    # - Inner except IndexError catches it.
    # - Prints caught IndexError.
    # - finally executes.
    # - Program continues and prints ....
# Case 2: noraise()
    # - Does not raise an exception.
    # - except does not execute.
    # - finally still executes.
    # - Program prints ....
# Case 3: raise2()
    # - Raises SyntaxError.
    # - except IndexError cannot catch it.
    # - finally still executes.
    # - SyntaxError propagates to the top-level handler.
    # - ... is not printed.
# Output:
    # <raise1>
    # caught IndexError
    # finally run
    # ...
    # <noraise>
    # finally run
    # ...
    # <raise2>
    # finally run
    # Traceback (most recent call last):
    # ...etc...
    # SyntaxError: None