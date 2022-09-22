a = 100
b = 400
while a <= b:
    z = a
    if (z % 10) % 2 == 0:
        z = z // 10
        if (z % 10) % 2 == 0:
            z = z // 10
            if z % 2 == 0:
                print(a)
                a += 1
            else:
                a += 1
        else:
            a += 1
    else:
        a += 1
