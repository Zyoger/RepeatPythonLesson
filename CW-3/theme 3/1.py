"""1. Дана последовательность чисел. Удалите из нее все положительные числа. Вычислите сумму отрицательных чисел и
 напечатайте ее абсолютное значение. Решите задачу с использованием lambda-функций."""

subsequence = [2, 4, -5, -7, -3, 5, 7, 9]

new_subsequence = list(filter(lambda i: i < 0, subsequence))
print(new_subsequence)
print(sum(new_subsequence))
