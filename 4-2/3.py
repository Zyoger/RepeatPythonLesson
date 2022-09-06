dat = ([1, 0, 0, 1, 1], [0, 1, 1, 1, 1], [1, 0, 1, 0, 0])
flag1 = flag2 = flag3 = 0

for d in dat:
    x1 = d[0]
    x2 = d[1]
    x3 = d[2]
    x4 = d[3]
    F = d[4]
    if ((x1 or not x2) and (not x3 or x4)) == F:
        flag1 += 1
    if ((not x1 or x3) and x2 or x4) == F:
        flag2 += 1
    if (x1 and x2 or (not x3 or (x1 or x4))) == F:
        flag3 += 1

print(flag1, flag2, flag3)
