
class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0(): raise General()
def raiser1(): raise Specific1()
def raiser2(): raise Specific2()

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General as X:            # X is the raised instance
        print('caught:', type(X))   # Same as sys.exc_info()[0], X.__class__

# - as X assigns the raised exception instance to X.
# - type(X) returns the class of that instance.
# - It gives the same result as sys.exc_info()[0] or X.__class__.
# Because except as provides direct access to the exception, sys.exc_info() is more useful
# for empty except clauses that do not otherwise provide access to the instance.
