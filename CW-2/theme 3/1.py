"""1. Определить, сколько раз последовательность из N произвольных чисел меняет знак
(т.е. после положительного элемента идет отрицательный и наоборот)"""
p = [3, -4, -14, 67, 28, -56, -34, 6, -7, 3]
count = 0
for i in range(len(p)-1):
    if (p[i] > 0 and p[i+1] < 0) or (p[i] < 0 and p[i+1] > 0):
        count += 1
        i += 1
    else:
        i += 1

print("n =", count)
