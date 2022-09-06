import itertools
variations = list(itertools.product((True, False), repeat=3))
print(variations)

A = None
B = None
C = None

for var in variations:
    A = var[0]
    B = var[1]
    C = var[2]
    f1 = B and not A and not C
    f2 = C and not A and not B
    f3 = not B and (A or C)
    f4 = (f1 and f2 and not f3) or (f1 and not f2 and f3) or (not f1 and f2 and f3)
    if f4:
        print(A, B, C)
