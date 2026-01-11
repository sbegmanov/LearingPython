# while Loops

while True:
    print('Type Ctrl+C to stop me')

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

while test:
 statements
 if test: break # Exit loop now, skip else if present
 if test: continue # Go to test at top of loop now
else:
 statements # Run on exit if didn't hit a 'break'

while True: pass # Type Ctrl+C to stop me!

def func1():
 pass # Add real code here later
