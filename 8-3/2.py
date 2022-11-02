class Matrix:
    count_create_matrix = 0
    count_identity_matrix = 0
    count_null_matrix = 0
    count_diagonal_matrix = 0

    def set(self, dimension, elements):
        self.dimension = dimension
        self.elements = elements
        Matrix.count_create_matrix += 1
        self.counter_property()

    def counter_property(self):
        matrix = self.elements
        if self.identity_matrix():
            Matrix.count_identity_matrix += 1
        if self.null_matrix():
            Matrix.count_null_matrix += 1
        if self.diagonal_matrix():
            Matrix.count_diagonal_matrix += 1

    def print_property(self):
        print(f"Всего создано {self.count_create_matrix} матриц.")
        print(f"Количество единичных матриц: {self.count_identity_matrix}")
        print(f"Количество нулевых матриц: {self.count_null_matrix}")
        print(f"Количество диагональных матриц: {self.count_diagonal_matrix}")

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
copy_class.set([4, 4], [[9, 2, 3],
                        [6, 7, 8],
                        [0, 1, 2]])
copy_class.print()
copy_class.get_matrix_determinant()
copy_class.print_property()
# print(copy_class.identity_matrix())
# print(copy_class.null_matrix())
# print(copy_class.diagonal_matrix())


