class Matrix:
    count_create_matrix = 0
    count_identity_matrix = 0
    count_null_matrix = 0
    count_diagonal_matrix = 0

    def __new__(cls, *args, **kwargs):
        print("Это конструктор!!!")
        return super().__new__(cls)

    def __init__(self, dimension, elements):
        print("Это инициализатор!!!")
        self.dimension = dimension
        self.elements = elements
        self.inc_count(elements)

    def __del__(self):
        print("Это деструктор!!!")

    @classmethod
    def inc_count(cls, matrix):
        Matrix.count_create_matrix += 1
        if Matrix.identity_matrix(matrix):
            Matrix.count_identity_matrix += 1
        if Matrix.null_matrix(matrix):
            Matrix.count_null_matrix += 1
        if Matrix.diagonal_matrix(matrix):
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

    @staticmethod
    def identity_matrix(matrix):
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

    @staticmethod
    def null_matrix(matrix):
        flag = True
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] != 0:
                    flag = False
        return flag

    @staticmethod
    def diagonal_matrix(matrix):
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


copy_class = Matrix([3, 3], [[9, 2, 3], [6, 7, 8], [0, 1, 2]])
copy_class.print()
copy_class.get_matrix_determinant()
copy_class.print_property()
# print(copy_class.identity_matrix())
# print(copy_class.null_matrix())
# print(copy_class.diagonal_matrix())


