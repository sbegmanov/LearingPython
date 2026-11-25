
class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

# 1. Exception hierarchy
# General is the superclass and represents the general exception category.
# Specific1 and Specific2 are subclasses representing specific exceptions.
# All three inherit from the built-in Exception class, which is required for normal exception handling.

def raiser0():
    X = General()           # Raise superclass instance
    raise X

# 2. Raising instances
# - General() creates an exception instance.
# - raise X raises that instance.
# - The other functions raise instances of Specific1 and Specific2.
# An exception instance can be created before raise or directly inside it

    # When raise X runs:
    # 1. Execution of the try block is interrupted.
    # 2. Python looks for a matching except clause.
    # 3. except General matches the raised General instance (and its subclasses).
    # 4. Python executes the except block.

def raiser1():
    X = Specific1()         # Raise subclass instance
    raise X

def raiser2():
    X = Specific2()         # Raise different subclass instance
    raise X

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:         # Match General or any subclass of it
        import sys
        print('caught:', sys.exc_info()[0])

# 3. Catching categories
# Each function raises a different exception.
# except General catches all three because Specific1 and Specific2 inherit from General.
# sys.exc_info()[0] returns the class of the raised exception

# 4. Accessing exception details with sys.exc_info()
# sys.exc_info() returns a tuple:
# - First item: exception class.
# - Second item: actual exception instance.
# This allows a general exception handler to identify exactly which exception occurred.