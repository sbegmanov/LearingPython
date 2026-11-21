
sep = '-' * 45 + '\n'

print(sep + 'EXCEPTION RAISED AND CAUGHT')
try:
    x = 'hack'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

print(sep + 'EXCEPTION NOT RAISED')
try:
    x = 'hack'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

print(sep + 'EXCEPTION NOT RAISED, WITH ELSE')
try:
    x = 'hack'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
try:
    x = 1 / 0
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

# Case 1: Exception raised and caught
# - 'hack'[99] raises IndexError because the index doesn't exist.
# - except catches it.
# - finally executes.
# - Execution continues with after run.

# Case 2: Exception not raised
# - 'hack'[3] is valid.
# - except is skipped.
# - finally executes.
# - Execution continues.

# Case 3: No exception, with else
# - 'hack'[3] is valid.
# - except is skipped.
# - else executes.
# - finally executes.

# Case 4: Exception raised but not caught
# - 1 / 0 raises ZeroDivisionError.
# - except IndexError cannot catch it.
# - finally still executes.
# - Python propagates the exception and terminates the program.