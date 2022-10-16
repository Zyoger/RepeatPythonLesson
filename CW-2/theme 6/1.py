"""1. Преобразуйте матрицу A(n, m) таким образом, чтобы строки с нечетными индексами были упорядочены по убыванию,
 а с четными - по возрастанию."""
matrix = [[2, 4, 1, 6], [4, 7, 3, 9], [2, 7, 4, 8], [8, 5, 4, 3]]
for s in matrix:
    print(s)

for i in range(len(matrix)):
    if i % 2 == 0:
        matrix[i].sort(reverse=True)
    else:
        matrix[i].sort()

print("-"*10)
for s in matrix:
    print(s)
