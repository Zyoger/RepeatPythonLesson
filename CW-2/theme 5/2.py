"""2. Дана последовательность чисел. Проверить, являются ли все элементы последовательности нечетными числами."""

subsequence = [41, 20, 15, 71, 45, 73, 33, 93]
flag = True
for elem in subsequence:
    if elem % 2 == 0:
        flag = False
        break
if flag:
    print("да")
else:
    print("нет")
