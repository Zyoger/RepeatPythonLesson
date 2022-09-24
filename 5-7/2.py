matrix = [[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]
flag = False
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if i == j:
            if matrix[i][j] != 1:
                flag = True
                print("Не единичная")
                break
        else:
            if matrix[i][j] != 0:
                flag = True
                print("Не единичная")
                break
    if flag:
        break
else:
    print("Единичная")

