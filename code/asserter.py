
def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2

# assert x < 0 checks whether x is negative.
# If x is negative, execution continues.
# If x is positive, Python raises AssertionError.