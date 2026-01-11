# state = 1 or
# [1, 2, 3] or [0, 2, 3] or (1, 2, 3) or (0, 2, 3) or
# dict(a=1, b=2, c=3) or dict(a=0, b=2, c=3) or other

match state:
    case 1 | 2 | 3 as what: # Match integer literals, what = 1
        print('or', what)
    case [1, 2, what]: # Match sequence (1), what = 3
        print('list', what)
    case [0, *what]: # Match sequence (0), what = [2, 3]
        print('list', what)
    case {'a': 1, 'b': 2, 'c': what}: # Match mapping, what = 3
        print('dict', what)
    case {'a': 0, **what}: # Match mapping, what = {'b': 2, 'c': 3}
        print('dict', what)
    case (1, 2, what):
        print('tuple', what)
    case (0, *what): # Match sequence: same as [0, *what]
        print('tuple', what)
    case _ as what:
        print('other', what)

# Attribute and instance patterns 
class Emp:
    def __init__(self, name):
        self.name = name
pat = Emp('Pat') # pat.name becomes 'Pat'

# state = 'Pat' or pat
match state:
    case pat.name as what:  # Match object's attribute, what = 'Pat'
        print('attr', what)
    case Emp(name=what):    # Match an Emp instance, what = 'Pat'
        print('instance', what)

# nested structures match 
state = ((1, 2), 3)
guard1 = True # a=1, b=3 if True; a=(1, 2) if False

match state:
    case ((a, 2), b) if guard1: # Match+run only if guard1 is True
        print(f'case1 {a=} {b=}')
    case (a, 3) as what: # Reached only if guard1 is False
        print(f'case2 {a=} {what=}')
    case [a, (3 | 4)] as what if guard1:
        print(f'case3 {a=} {what=}')
