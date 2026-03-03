import first

# 1 way
print(first.X) # OK: references a name in another file
first.X = 88 # But changing it can be too subtle and implicit

# 2 way
first.setX(88) # Call the function instead of changing directly