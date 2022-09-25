matrix = [[1, 2, 6, 2],
          [2, 1, 8, 3],
          [6, 8, 2, 7],
          [2, 3, 7, 1]]
flag = True
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] != matrix[j][i]:
            flag = False
            break

if flag:
    print("Матрица симметричная")
else:
    print("Не симметричная")
