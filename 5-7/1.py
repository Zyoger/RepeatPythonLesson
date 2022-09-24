matrix = [[3, 4, 5, 6],
          [4, 5, 6, 7],
          [2, 9, 3, 6],
          [5, 8, 8, 1]]
print(matrix)
max_element = 0
max_position = [None, None]
min_element = sum(matrix[0]) + sum(matrix[1]) + sum(matrix[2]) + sum(matrix[3])
min_position = [None, None]

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] > max_element:
            max_element = matrix[i][j]
            max_position[0] = i
            max_position[1] = j
        if matrix[i][j] < min_element:
            min_element = matrix[i][j]
            min_position[0] = i
            min_position[1] = j

print(max_element)
print(max_position)
print(min_element)
print(min_position)
matrix[max_position[0]][max_position[1]], matrix[min_position[0]][min_position[1]] = matrix[min_position[0]][min_position[1]], matrix[max_position[0]][max_position[1]]
print(matrix)
