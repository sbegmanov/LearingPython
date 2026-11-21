
def gobad(x, y):
    return x / y
def gosouth(x):
    print(gobad(x, 0))

if __name__ == '__main__': gosouth(1)

# Here:
# - gosouth(1) calls gobad(1, 0).
# - gobad() attempts to divide by zero.
# - Python raises ZeroDivisionError.
# - No try statement catches it, so the program terminates.