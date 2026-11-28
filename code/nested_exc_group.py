
def action3():
    raise ExceptionGroup('Nest*', [IndexError(1), TypeError(2), SyntaxError(3)])

def action2():
    try:
        action3()
    except* IndexError:         # Consume matches, rest propagate
        print('Got IE')

def action1():
    try:
        action2()
    except* TypeError:          # Consume matches, rest propagate
        print('Got TE')

if __name__ == '__main__': action1()

# How it works:
    # Initially, the exception group contains three exceptions:
    # Original exception group: Nest*
    # IndexError(1)  Consumed by action2
    # TypeError(2)   Consumed by action1
    # SyntaxError(3) Unmatched
# 1. action1() calls action2().
# 2. action2() calls action3(), which raises the group containing three exceptions.
# 3. The except* IndexError handler in action2() consumes IndexError and prints Got IE.
# 4. The remaining TypeError and SyntaxError propagate to action1().
# 5. The except* TypeError handler in action1() consumes TypeError and prints Got TE.
# 6. SyntaxError remains unmatched and propagates to the top-level handler.

# Got IE
# Got TE
#  + Exception Group Traceback (most recent call last):
#  ...
#  | ExceptionGroup: Nest* (1 sub-exception)
#  +-+---------------- 1 ----------------
#  | SyntaxError: 3
#  +------------------------------------