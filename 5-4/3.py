l = [31, 59, 7, 89, 98, 11, 12, 13]
summa = 0
for i in l:
    flag = True
    for n in range(2, i):
        if i % n == 0:
            flag = False
    if flag:
        summa += 1
print("Количество:", summa)
