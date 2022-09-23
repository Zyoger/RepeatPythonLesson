n = 17
flag = 0
for i in range(2, n):
    if n % i == 0:
        flag += 1
if flag == 0:
    print("Число простое")
else:
    print("Число не простое")
