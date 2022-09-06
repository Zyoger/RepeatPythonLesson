import itertools
array = list(itertools.product((True, False), repeat=4))

for arg in array:
    K = arg[0]
    L = arg[1]
    M = arg[2]
    N = arg[3]
    if not ((not K or M) or (not L or M or N)):
        print(f"Искомая комбинация: K = {K}, L = {L}, M = {M}, N = {N}")
