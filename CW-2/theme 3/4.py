"""4. Найти среднее арифметическое делителей числа N."""
N = 120
divider = 0
summa = 0
for i in range(1, int(N/2)+1):
    if N % i == 0:
        divider += 1
        print(i)
        summa += i
        i += 1
print("------")
print(summa)
print(divider)
print(summa/divider)
