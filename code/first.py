# for 1 was
X = 99 # This code doesn't know about second.py

# 2 way
def setX(new): # Accessors make external changes explicit
    global X # And can manage access in a single place
    X = new
