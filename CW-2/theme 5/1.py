"""1. Дана последовательность чисел. Проверить, есть ли в ней хотя бы одно число с делителями 2, 5 и 7. Если да,
вывести его на экран. Если нет, вывести соответствующее сообщение."""
subsequence = [4, 20, 15, 70, 45, 76, 34, 90]
result = None
for elem in subsequence:
    if elem % 2 == 0 and elem % 5 == 0 and elem % 7 == 0:
        result = elem
if result is None:
    print("Элементов нет")
else:
    print(result)
