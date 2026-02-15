# Iterations
for x in [1, 2, 3, 4]: print(x ** 2, end=' ')
for x in (1, 2, 3, 4): print(x ** 3, end=' ')
for x in 'text': print(x * 2, end=' ')
for k in dict(a=1, b=2, c=3): print(k, end=' ')

# The Iteration Protocol
print(open('data.txt').read())
open('data.txt').read()

f = open('data.txt') # Read a three-line file in this directory
f.readline() # readline loads one line on each call
f.readline() # Newlines are \n everywhere in text mode
f.readline() # Last lines may have a \n or not
f.readline() # Returns empty string at end-of-file

f = open('data.txt') # __next__ loads one line on each call too
f.__next__() # But raises an exception at end-of-file
f.__next__()
f.__next__()
f.__next__()

for line in open('data.txt'): # Use file iterators to read by lines
    print(line.upper(), end='') # Calls __next__, catches StopIteration

 for line in open('data.txt').readlines():
     print(line.upper(), end='')


f = open('data.txt')
while line := f.readline():
    print(line.upper(), end='')


## The iter and next built-ins
f = open('data.txt')
f.__next__() # Call iteration method directly
next(f) # next(f) is the same as f.__next__()
next(f)

f = open('data.txt')
I = iter(f) # Fetch an iterator from an iterable
next(I) # Fetch the next result from the iterator
next(I) # Files iterables are iterators themselves

## The full iteration protocol
L = [1, 2]
I = iter(L) # Obtain an iterator object from an iterable
next(I) # Call next(iterator) to advance to next item
next(I) # Or use L.__iter__() and I.__next__() calls
next(I)

f = open('data.txt')
iter(f) is f # Files are iterators themselves: iter() optional
iter(f) is f.__iter__() # Both calls return file object f itself
next(f) # Which responds to next requests directly

L = [1, 2, 3]
iter(L) is L # Lists are not their own iterators: use iter()
next(L)
I = iter(L) # Same as L.__iter__()
next(I) # Same as I.__next__()

## Manual iteration
L = [1, 2, 3]
for X in L: # Automatic iteration
    print(X ** 2, end=' ') # Obtain iter, call __next__, catch exceptions

I = iter(L) # Manual iteration: what for loops usually do
while True: # Use try statements to catch stop exception
    try:
        X = next(I)
    except StopIteration:
        break
    print(X ** 2, end=' ')

# More on iter and next
L = [1]
I = iter(L) # Result instead of exception
next(I, 'end of list')
next(I, 'end of list')

I = iter(L)
while (X := next(I, None)) != None: # Same effect, less code
    print(X ** 2, end=' ') # Assuming None is safe!

f = open('data.txt')
I = iter(lambda: f.read(5), '') # Callables and sentinels
for block in I: print(block, end='') # Assuming you know lambda!

# Other Built-in Iterables
# Reprise: Dictionaries, range, enumerate, and zip
D = dict(a=1, b=2)
for key in D: # Dictionaries are implicitly iterable
    print(key, D[key])

I = iter(D) # Which just means they support the protocol
next(I)
next(I)
next(I)

R = range(5)
range(0, 5)
I = iter(R) # Use iteration protocol to produce results
next(I)
next(I)
list(range(5)) # Or use list() to collect all results at once

E = enumerate('text') # enumerate is an iterable too
I = iter(E)
next(I) # Generate results with iteration protocol
next(I) # Or use list() to force generation to run
list(enumerate('text'))

R = range(5)
iter(R) is R
E = enumerate('text')
iter(E) is E
next(E)

Z = zip((1, 2, 3), (10, 20, 30))
I = iter(Z)
next(I)
next(I)
I is Z
list(Z)
list(zip((1, 2, 3), (10, 20, 30)))

# Iterator nesting
Z = zip(range(1, 4), range(10, 40))
next(Z)
next(Z)
next(Z)
list(zip(range(1, 4), range(10, 40)))
list(enumerate(range(1, 4)))
list(zip(enumerate(range(1, 4)), enumerate(range(5, 8))))
for x in enumerate(zip(range(1, 4), range(5, 8))): print(x)

# Functional iterables: map and filter
ord('p') # Return a single character's code point
M = map(ord, 'py3') # map returns an iterable, not a list
next(M)  # Iterating manually: exhausts results

list(map(ord, 'py3'))  # Force a real list - only if needed
M = map(ord, 'py3')  # Must call again to scan again
for x in M: print(x, end=' ')  # Iteration tools auto call next()

filter(bool, ['lp6e', '', 2024])
list(filter(bool, ['lp6e', '', 2024]))  # Collect "true" items
list(filter(str.isdigit, ['lp6e', '2024']))  # Collect all-digit strings
[ord(x) for x in 'py3']
[x for x in ['lp6e', '2024'] if x.isdigit()]

# Multiple-pass versus single-pass iterables
R = range(3)  # range allows multiple iterators
next(R)

I1 = iter(R)
next(I1)
I2 = iter(R) # Two iterators on one range
next(I2)
next(I1)  # I1 is at a different spot than I2

Z = zip((1, 2, 3), (10, 11, 12))
I1 = iter(Z)
I2 = iter(Z)  # Two iterators on one zip
next(I1)
next(I1)
next(I2)  # But I2 is at same spot as I1!

M = map(ord, 'py3')  # Ditto for map (and others)
I1, I2 = iter(M), iter(M)
next(I1), next(I1)
next(I2)

L = [0, 1, 2]  # But lists (and others) do many scans
I1, I2 = iter(L), iter(L)
next(I1), next(I1)
next(I2) # Multiple active scans, like range

# Comprehensions
L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 10

L = [x + 10 for x in L]
res = []
for x in L:
    res.append(x + 10)

# List Comprehensions and Files
f = open('data.txt')
lines = f.readlines()
lines = [line.rstrip() for line in lines]
lines = [line.rstrip() for line in open('data.txt')]

[line.upper() for line in open('data.txt')]
[line.rstrip().upper() for line in open('data.txt')]
[line.split() for line in open('data.txt')]
[line.replace('\n', '!') for line in open('data.txt')]
[('Py' in line, line.split()[0]) for line in open('data.txt')]

# Extended List Comprehension Syntax
lines = [line.rstrip() for line in open('data.txt') if line[0] in 'LP']

res = []
for line in open('data.txt'):
    if line[0] in 'LP':
        res.append(line.rstrip())

[line.rstrip() for line in open('data.txt') if line.rstrip()[-1:].isdigit()]
fname = 'data-blank-lines.txt'
len(open(fname).readlines()) # All lines
len([line for line in open(fname) if line.strip() != '']) # Nonblank lines

# Nested loops: for
[x + y for x in 'abc' for y in '123']

res = []
for x in 'abc':
    for y in '123':
        res.append(x + y)

# Comprehensions Cliff-Hanger
[x + 10 for x in L if x > 0] # List comprehension
{x + 10 for x in L if x > 0} # Set comprehension
{x: x + 10 for x in L if x > 0} # Dictionary comprehension
(x + 10 for x in L if x > 0) # Generator expression

# Iteration Tools
for line in open('data.txt'):
    print(line.upper(), end='')

uppers = [line.upper() for line in open('data.txt')]
list(map(str.upper, open('data.txt')))

sorted(open('data.txt'))
list(zip(range(99), open('data.txt')))
list(enumerate(open('data.txt')))
list(filter(bool, open('data.txt')))

import functools, operator
functools.reduce(operator.add, open('data.txt'))

list(open('data.txt'))
tuple(open('data.txt'))
'&&'.join(open('data.txt'))

a, b, c = open('data.txt')  # Sequence assignment
a, *b = open('data.txt')  # Extended-unpacking assignment
'Python 2.7\n' in open('data.txt')  # Membership test
'Python 3.12\n' in open('data.txt')
L = [11, 22, 33, 44]  # Slice assignment
L[1:3] = open('data.txt')

L = [11]
L.extend(open('data.txt'))  # list.extend method
L = [11, *open('data.txt'), 44]  # List-literal unpacking

L = [11]
L.append(open('data.txt'))
list(L[-1])

set(open('data.txt'))
{line for line in open('data.txt')}
{ix: line for ix, line in enumerate(open('data.txt'))}
{line for line in open('data.txt') if line[0] in 'LP'}
{ix: line for (ix, line) in enumerate(open('data.txt')) if line[0] in 'LP'}
list(line.upper() for line in open('data.txt'))

sum(range(5)) # Punt (requires numbers)
any(open('data.txt')) # Any/all lines true (nonempty)
all(open('data.txt'))  # Mostly pointless for files
max(open('data.txt')) # Line with highest string value
min(open('data.txt'))  # Use cases wanted!


def f(a, b, c):  # See Part IV
    print(a, b, c, sep='&')
f(*open('data.txt'))  # Iterates by lines too!

X, Y = (1, 2), (3, 4)
list(zip(X, Y))  # Zip tuples: returns an iterable
A, B = zip(*zip(X, Y))  # Unzip a zip, really!




