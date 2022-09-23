p = [7, 5, 8, 9, 2, 3, 2, -2]
temp = sum(p)
for i in p:
    if i >= 0:
        if i < temp:
            temp = i