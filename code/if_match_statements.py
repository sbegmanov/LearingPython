choice = 'Windows'
print({'macos': 2001, 'Linux': 1991, 'Windows': 1985}[choice])

# The equivalent if statement
if choice == 'macros':
    print(2001)
elif choice == 'Linux':
    print(1991)
elif choice == 'Windows':
    print(1985)
else:
    print('Bad choice')

# Handling switch defaults
branch = dict(macos=2001, Linux=1991, Windows=1985)

print(branch.get('Windows', 'Bad choice'))
print(branch.get('Solaris', 'Bad choice'))

choice = 'AmigaOS'
if choice in branch:
    print(branch[choice])
else:
    print('Bad choice')

choice = 'GEM'
try:
    print(branch[choice])
except KeyError:
    print('Bad choice')

# match Statements
# state = 'go' or 'stop' or other

if state == 'go':
    print('green')
elif state == 'stop':
    print('red')
else:
    print('yellow')

colors = dict(go='green', stop='red')
print(colors.get(state, 'yellow'))

match state:
    case 'go':
        print('green')
    case 'stop':
        print('red')
    case _:                 # match anything
        print('yellow')


# state = 'go' or 'proceed' or 'start', or 'stop' or 'halt', or any other
match state:
    case 'go' | 'proceed' | 'start':
        print('green')
        print('means og')
    case 'stop' | 'halt' as what: # Match any, and assign it to what
        print('red')
        print('means', what)
    case other:
        print('catchall', other)
    
# Match versus if live
for stmt in ['if', 'while', 'try']:
    match stmt:
        case 'if' | 'match':
            print('logic')
        case 'for' | 'while' as which:
            print('loop')
        case other:
            print('tbd')

print(which, other)

for stmt in ['if', 'while', 'try']:
    if stmt in ['if', 'match']:
        print('logic')
    elif stmt in ['for', 'while']:
        which = stmt
        print('loop')
    else:
        other = stmt
        print('tbd')

# Block Delimiters: Indentation Rules
x = 1
if x:
    y = 2
    if y:
        print('block2')
    print('block1')
print('block0')

x = 'Hack'
if 'tho' in 'python':
    print(x * 8)
    x += 'More!'
    if x.endswith('re!'):
        x *= 2
    print(x)


L = ['app',
     'script',
     'program'] # Open pairs may span lines

# Special Syntax Cases in Action
if a == b and c == d and \
   d == e and f == g:
    print('old school') # Backslashes allow continuations...

if (a == b and c == d and
    d == e and e == f):
    print('new school') # But parentheses usually do too, and are obvious

x = 1 + 2 + 3 \ # Omitting the \ makes this very different!
+4

x = 1; y = 2; print(x) # More than one simple statement

S = """
aaaa
bbbb
cccc"""
S = ('aaaa' 
    'bbbb'          # Comments here are ignored, add \n if needed
    'cccc')
S = (f'{'a' * 4}'   # Also makes 'aaaabbbbcccc'
 f'{'b' * 4}'       # Use f'' on each f-string part
 r'cccc')           # And ditto for r'' raw-string parts

if 1: print('hello') # Simple statement on header line

# Truth Values Revisited (True or False return)
2 < 3, 3 < 2
2 or 3, 3 or 2
[] or 3
[] or {}
2 and 3, 3 and 2
[] and {}
3 and []

# The if/else Ternary Expression
if X:
    A = Y
else:
    A = Z

A = Y if X else Z

tone = 'formal'
a = 'code' if tone == 'formal' else 'hack'

tone = 'informal'
a = 'code' if tone == 'formal' else 'hack'

A = Y if X else Z # Ternary if/else
A = ((X and Y) or Z) # and+or equivalent
A = [Z, Y][bool(X)]

#False == 0, True  == 1
['hack', 'code'][tone == 'formal']
['hack', 'code'][bool('formal')]