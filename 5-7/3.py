matrix = [[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 10, 0],
          [0, 3, 0, 1]]
average = 0

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        average += matrix[i][j]
    else:
        average = average/len(matrix[i])
        matrix[i][0] = average
        average = 0

print(matrix)
