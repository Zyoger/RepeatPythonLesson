"""2. Дана квадратная матрица. Проверьте, является ли она диагональной."""
matrix = [[2, 0, 0, 0],
          [0, 7, 0, 0],
          [0, 0, 5, 0],
          [0, 0, 0, 3]]
flag = True
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j and matrix[i][j] == 0:
            flag = False
            break
        elif i != j and matrix[i][j] != 0:
            flag = False
            break
if flag:
    print("да")
else:
    print("нет")
