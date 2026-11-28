
def action3():
    print(1 + [])           # Generate TypeError

def action2():
    try:                    # Most recent matching try
        action3()
    except TypeError:
        print('Inner try')  # Match kills the exception
        raise               # Unless manually reraised

def action1():
    try:
        action2()
    except TypeError:
        print('Outer try')  # Run only if action2 reraises

if __name__ == '__main__': action1()

# How it works:
# 1. action1() enters its try and calls action2().
# 2. action2() enters its own try and calls action3().
# 3. action3() executes 1 + [], generating TypeError.
# 4. Python finds two active try statements, but chooses the most recent matching one: inside action2().
# 5. The inner handler prints Inner try.
# 6. raise reraises the same exception.
# 7. The exception propagates to action1(), where the outer handler catches it and prints Outer try.

# Output
# Inner try
# Outer try

# Important: raise
# - Without raise, the exception would be handled and propagation would stop inside action2().
# - With raise, the exception is sent to the next matching handler.