class Matrix:
    elements = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]]
    dimension = [4, 4]

    def print(self):
        matrix = self.elements
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end=" ")
            print()

    def get_matrix_determinant(self):
        matrix = self.elements
        if len(matrix) == 2:
            determinant_matrix = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            print("Данная матрица имеет размерность 2х2.")
            print(f"Определитель для матрицы равен: {determinant_matrix}")
        elif len(matrix) == 3:
            determinant_matrix = matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] \
                               + matrix[0][2] * matrix[1][0] * matrix[2][1] - matrix[0][2] * matrix[1][1] * matrix[2][0] \
                               - matrix[0][0] * matrix[1][2] * matrix[2][1] - matrix[0][1] * matrix[1][0] * matrix[2][2]
            print("Данная матрица имеет размерность 3х3.")
            print(f"Определитель для матрицы равен: {determinant_matrix}")
        else:
            print("Параметры данной матрицы не подходят для определения определителя.")

    def identity_matrix(self):
        matrix = self.elements
        flag = True
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if i == j:
                    if matrix[i][j] != 1:
                        flag = False
                if i != j:
                    if matrix[i][j] != 0:
                        flag = False
        return flag

    def null_matrix(self):
        matrix = self.elements
        flag = True
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] != 0:
                    flag = False
        return flag

    def diagonal_matrix(self):
        matrix = self.elements
        flag = True
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if i == j:
                    if matrix[i][j] == 0:
                        flag = False
                if i != j:
                    if matrix[i][j] != 0:
                        flag = False
        return flag


copy_class = Matrix()
copy_class.print()
copy_class.get_matrix_determinant()
print(copy_class.identity_matrix())
print(copy_class.null_matrix())
print(copy_class.diagonal_matrix())
