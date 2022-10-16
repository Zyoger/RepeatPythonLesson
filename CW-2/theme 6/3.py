"""3. Дана квадратная матрица. Проверьте, является ли она нижнетреугольной. Если да, преобразуйте ее таким образом,
 чтобы она стала верхнетреугольной."""
matrix = [[2, 1, 2, 4],
          [0, 7, 4, 5],
          [0, 0, 5, 4],
          [0, 0, 0, 3]]
flag = True
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i <= j and matrix[i][j] <= 0:
            flag = False
        if i > j and matrix[i][j] != 0:
            flag = False
print(flag)
if flag:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < j and matrix[i][j] > 0:
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = 0

for m in matrix:
    print(m)


"""    
ij ij ij ij

00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33
"""