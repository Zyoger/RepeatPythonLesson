import itertools
array = list(itertools.product((True, False), repeat=3))
print(array)
print(len(array))
for arg in array:
    if not (not arg[0] or (arg[2] and arg[0]) or (arg[1] and not arg[2])):
        print(arg)

