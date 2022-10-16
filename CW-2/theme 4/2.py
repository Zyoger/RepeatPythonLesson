"""2. Вычислить произведение последних трех чисел не кратных 5 в диапазоне от 20 до 50."""
count = 0
result = 1
for i in range(50, 19, -1):
    print(i)
    if i % 5 != 0:
        count += 1
        result *= i
    if count == 3:
        break
print(result)
