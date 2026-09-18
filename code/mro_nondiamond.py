
class E: attr = 'E'     # D     E
class D: attr = 'D'     # |     |
class C(E): attr = 'C'  # B     C
class B(D): pass        # \     /
class A(B, C): pass     #    A
                        #    |
X = A()                 #    X
print(X.attr)   # D


# DFLR => [X, A, B, D, object, C, E, object]
# MRO  => [X, A, B, D, C, E, object]

class D: attr = 'D'     #    D
class C(D): attr = 'C'  #   / \
class B(D): pass        #   B  C
class A(B, C): pass     #   \  /
                        #     A
X = A()                 #     |
print(X.attr) # C       #     X

# DFLR => [X, A, B, D, object, C, D, object]
# MRO => [X, A, B, C, D, object]
