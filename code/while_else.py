# while Loops

# while True:
#     print('Type Ctrl+C to stop me')

x = 'code'
while x:
    print(x, end=' ')
    x = x[1:]

a=0; b=10
while a < b:
    print(a, end=' ')
    a += 1

# while True:
#  …loop body… # Always run loop body at least once
#  if test: break # Test for loop exit at the bottom

# break, continue, pass, and the Loop else
test = 0
statements = 0

while test:
 statements
 if test: break # Exit loop now, skip else if present
 if test: continue # Go to test at top of loop now
else:
 statements # Run on exit if didn't hit a 'break'

# while True: pass # Type Ctrl+C to stop me!

# def func1():
#  pass # Add real code here later

# The nested-code alternative
x = 10
while x:
   x -= 1
   if x % 2 != 0: continue
   print(x, end=' ')

# break
num = 1
while True:
   tool = input(f'{num} What\'s your favorite language? ')
   if tool == 'stop': break
   print('Bravo!' if tool == 'Python' else 'Try again..')
   num += 1

# Named-assignment expressoin
num = 1
while (tool := input(f'{num} what\'s your favorite language ? ')) != 'stop':
   print('Bravo !' if tool == 'Python' else 'Try again...')
   num += 1

# Loop else

# while continuing:
#     if found:
#         found code
#         break
#     else advance
# else:
#     not-found code

##
x = num // 2
while x > 1:
   if num % x == 0:
      print(num, 'has factor', x)
      break
   x -= 1
else:
   print(num, 'is prime')

##
found = False
while x and not found:
   if match(x[0]): # Value at front?
      print('Found')
      found = True
   else:
      x = x[1:]
if not found: # Slice off front and repeat
   print('Not found')

##
while x:              # Exit when x empty
   if match(x[0]):
      print('Found')
      break           # Exit, go around else
   x = x[1:]
else:
   print('Not found') # Only here if exhausted x


## for Loops

for target in object:   # Assign object items to target
   statements           # Repeated loop body: use target
else:                   # Optional else
   statements           # Run if didn't exit loop body with break

for target in object:   # Assign object items to target
   statements
   if test: break       # Exit loop now, skip else
   if test: continue    # Go to top of loop now
else:
   statements           # Run on exit if didn't hit a 'break'

for x in ['app', 'script', 'program']:
   print(x, end=' ')

sum = 0
for x in [1, 2, 3, 4]:
   sum = sum + x

prod = 1
for item in [1, 2, 3, 4]:
   prod *= item


S = 'Python'
T = ('web', 'num', 'app')
for x in S: print(x, end=' ') # Iterate over a string
for x in T: print(x, end=' ') # Iterate over a tuple

# Tuple (sequence) assignment in for loops
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T: # Tuple assignment at work
   print(a, b)

# for [a, b] in T: # List assignment: same effect
# for a, b in T: # Tuple sans parentheses: same effect

D = {'a': 1, 'b': 2}
for key in D:
   print(key, '=>', D[key])   # Use dict keys iterator and index

list(D.items())

for (key, value) in D.items(): # Iterate over both keys and values
   print(key, '=>', value)

for both in T:
   a, b = both    # Manual assignment equivalent
   print(a, b)

((a, b), c) = ((1, 2), 3) # Nested sequences work too
print(a, b, c)

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)
for ((a, b), c) in [([1, 2], 3), ['XY', 6]]: print(a, b, c)


# Extended-unpacking assignment in for loops
a, b, c = (1, 2, 3) # Tuple assignment

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:  # Used in for loop
   print(a, b, c)

a, *b, c = (1, 2, 3, 4) # Extended-unpacking assignment

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
   print(a, b, c)

 for all in [(1, 2, 3, 4), (5, 6, 7, 8)]: # Manual slicing version
    a, b, c = all[0], all[1:-1], all[-1]
    print(a, b, c)

L, M = [1, 2], [3, 4]
pairs = [[(5, 6), (7, 8), (9, 10)]] * 2

for [(a, *X), (b, *L[0]), (c, *M[:0])] in pairs:
    print(f'<{a=} {X=}> <{b=} {L=}> <{c=} {M=}>')

# Nested for loops
for x in 'abc': # For each item in one string
   for y in '123': # And for each item in another string
      print(x + y, end=' ') # Concatenate current items from both


items = ['aaa', 111, (4, 5), 2.01] # A list of objects
tests = [(4, 5), 3.14] # Keys to search for
for key in tests: # For all keys
   for item in items: # For all items
      if item == key: # Check for match
         print(key, 'was found')
         break
   else:
      print(key, 'not found!')

 for key in tests: # For all keys
    if key in items: # Let Python check for a match
       print(key, 'was found')
    else:
       print(key, 'not found!')


seq1 = 'trippy'
seq2 = 'python'

res = [] # Start empty
for x in seq1: # Scan first sequence
   if x in seq2: # Common item?
      res.append(x) # Add to result end
print(res)

list(set(seq1) & set(seq2)) # Real intersection with sets
[x for x in seq1 if x in seq2]  # Let Python collect results

# Counter Loops: range
list(range(5)), list(range(2, 5)), list(range(0, 10, 2))
range(5)[2], range(5)[1:3], list(range(5)) + [6, 7]
range(5) + [6, 7] # TypeError

list(range(-5, 5))
list(range(5, -5, -1))

for i in range(3):
   print(i, 'Pythons')

# Sequence Scans: while, range, and for
X = 'hack'
for item in X: print(item, end=' ') # Automatic iteration with for

i = 0
while i < len(X): # Manual iteration with while
   print(X[i], end=' ')
   i += 1

i = -1
while (i := i + 1) < len(X): # Manual, but with := operator
   print(X[i], end=' ')


list(range(len(X)))
for i in range(len(X)): print(X[i], end=' ') # Manual range/len iteration
for item in X: print(item, end=' ') # Use auto iteration if you can

# Sequence Shufflers: range and len
S = 'hack'
for i in range(len(S)): # For repeat counts 0..3
   S = S[1:] + S[:1] # Move front item to end
   print(S, end=' ')

 for i in range(len(S)): # For positions 0..3
    X = S[i:] + S[:i] # Rear part + front part
    print(X, end=' ')

L = [1, 2, 3, 4]
for i in range(len(L)):
   X = L[i:] + L[:i] # Works on any sequence type
   print(X, end=' ')

# Skipping Items: range and Slices
S = 'abcdefghijk'
list(range(0, len(S), 2))
for i in range(0, len(S), 2): print(S[i], end=' ')
for c in S[::2]: print(c, end=' ')

# Changing Lists: range and Comprehensions
L = [10, 20, 30, 40, 50]
for x in L:
   x += 1  # Changes x, not L!

for i in range(len(L)): # Add one to each item in L
   L[i] += 1 # Or L[i] = L[i] + 1

i = 0
while i < len(L):  # And similar with := assignment
   L[i] += 1
   i += 1

[x + 1 for x in L]

# Parallel Traversals: zip
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

zip(L1, L2)  # An iterable that generates pairs
list(zip(L1, L2)) # list() required to see all results

for (x, y) in zip(L1, L2):
   print(f'{x} + {y} => {x + y}')

i = -1
while (i := i + 1) < len(L1):
   print(f'{L1[i]} + {L2[i]} => {L1[i] + L2[i]}')

# More on zip: size and truncation
list(zip(range(4), 'hack'))

T1, T2, T3 = (1, 2, 3), (4, 5, 6), (7, 8, 9) # 3 args of 3 vals => 3 3-item tuples
list(zip(T1, T2, T3))
list(zip(T1, T2))  # 2 args of 3 vals => 3 2-item tuples

S1 = 'abc'
S2 = 'xyz123'
list(zip(S1, S2)) # Truncates at len(shortest)

# More zip roles: dictionaries
D1 = {'app': 1, 'script': 3, 'program': 5}  # Or dict(key=value,…)

keys = ['app', 'script', 'program']
vals = [1, 3, 5]
list(zip(keys, vals))

D2 = {}
for (k, v) in zip(keys, vals): D2[k] = v

D3 = dict(zip(keys, vals))
{k: v for (k, v) in zip(keys, vals)}

# Offsets and Items: enumerate
S = 'hack'
offset = 0
for item in S:
   print(item, 'appears at offset', offset)
   offset += 1

S = 'hack'
for (offset, item) in enumerate(S):
   print(item, 'appears at offset', offset)

E = enumerate(S)
next(E)

[c * i for (i, c) in enumerate(S)]

for (ix, line) in enumerate(open('data\data.txt')):
   print(f'{ix}) {line.rstrip()}')

