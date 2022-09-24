numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total_iterations = 0
summa = 0

for i in numbers:
    summa += i
    total_iterations += 1
    if summa >= 15:
        break

print("Результат:", summa)
print("Всего итераций:", total_iterations)
print()

total_iterations_1 = 0
summa_1 = 0
n = 0

while n <= len(numbers):
    summa_1 += numbers[n]
    n += 1
    total_iterations_1 += 1
    if summa_1 >= 15:
        break

print("Результат:", summa_1)
print("Всего итераций:", total_iterations_1)
