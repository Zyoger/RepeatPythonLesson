matrix = [[1, 2, 6, 2],
          [0, 1, 8, 3],
          [0, 0, 2, 7],
          [0, 0, 0, 1]]
flag = True
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if i <= j and matrix[i][j] <= 0:
            flag = False
            break
        elif i > j and matrix[i][j] > 0:
            flag = False
            break

if flag:
    print("Верхнеугольная")
else:
    print("Не верхнеугольная")
