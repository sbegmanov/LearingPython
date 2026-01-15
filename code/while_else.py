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

while continuing:
    if found: 
        found code
        break
    else advance
else:
    not-found code

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

