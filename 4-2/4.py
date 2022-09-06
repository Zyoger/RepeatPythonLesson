import itertools
array = list(itertools.product((1, 0), repeat=4))
flag = 0

for arg in array:
    a = arg[0]
    b = arg[1]
    c = arg[2]
    d = arg[3]
    if not ((a and not b) or (not a and b)) or (c and d):
        flag += 1

print(flag)