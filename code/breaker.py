
class Exitloop(Exception): pass

try:
    while True:
        while True:
            for i in range(10):
                if i > 3: raise Exitloop    # break exits just one level
                print('loop3: %s' % i)      # raise can exit many

            print('loop2')
        print('loop1')
except Exitloop:
    print('continuing')                     # Or just pass, to move on

print(f'{i=}')                              # Loop variable not undone

# 3. How it works
# 1. Exitloop defines a custom exception.
# 2. Three nested loops start executing.
# 3. The for loop assigns values to i: 0, 1, 2, 3, ...
# 4. When i becomes 4, the condition i > 3 becomes true.
# 5. raise Exitloop immediately raises the exception.
# 6. Python exits all three loops and jumps to except Exitloop.
# 7. The handler prints continuing.
# 8. Execution continues after the try/except statement

# loop3: 0
# loop3: 1
# loop3: 2
# loop3: 3
# continuing
# i=4         # i=4 (the final value) means the loop variable i had the value 4 when the exception occurred.

# 4. Why not use break?
# If you replace: raise Exitloop
# with: break
# Python exits only the innermost for loop.
# Then:
# - The program prints loop2.
# - The second-level while loop continues.
# - The for loop starts again.
# - This repeats indefinitely.
# You would need to press Ctrl+C to stop the program.

# 5. What happens to variable i?
# Notice the final output: i=4
# The variable i still exists after the try statement exits.
# The book explains:
# - Variable assignments made inside try are not automatically undone.
# - Exception variables introduced using as in an except header are localized to that clause.
# - Local variables belonging to functions exited because of raise are discarded.
