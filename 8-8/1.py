import math
from math import sqrt


class Quadrilateral:
    # [x, y]

    def __init__(self, point_1, point_2, point_3, point_4):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.point_4 = point_4

    def checks_existence(self) -> bool:
        a, b, c, d = Quadrilateral.get_side_lengths(self.point_1, self.point_2, self.point_3, self.point_4)
        return a < b + c + d and b < a + c + d and c < a + b + d and d < a + b + c

    def print(self):
        print(f"Координаты точек: {self.point_1} {self.point_2} {self.point_3} {self.point_4}")
        print("Прямоугольник существует!" if self.checks_existence() else "Прямоугольник не существует!")
        print(f"Длины сторон: {Quadrilateral.get_side_lengths(self.point_1, self.point_2, self.point_3, self.point_4)}")
        print(f"Периметр равен: {self.get_perimetr()}")
        print(f"Площадь равна: {self.get_area()}")
        print(f"Диагональ равна: {self.get_diagonal()}")

    @staticmethod
    def get_side_lengths(point_1, point_2, point_3, point_4):
        a = Quadrilateral.calculate_side(point_2, point_1)
        b = Quadrilateral.calculate_side(point_3, point_2)
        c = Quadrilateral.calculate_side(point_3, point_4)
        d = Quadrilateral.calculate_side(point_4, point_1)
        return [a, b, c, d]

    @staticmethod
    def calculate_side(point_1, point_2):
        return sqrt((point_2[1] - point_1[1])**2 + (point_2[0] - point_1[0])**2)

    def get_diagonal(self):
        a, b, c, d = Quadrilateral.get_side_lengths(self.point_1, self.point_2, self.point_3, self.point_4)
        return round(sqrt(a ** 2 + b ** 2), 3)

    def get_perimetr(self):
        a, b, c, d = Quadrilateral.get_side_lengths(self.point_1, self.point_2, self.point_3, self.point_4)
        return a + b + c + d

    def get_area(self):
        a, b, c, d = Quadrilateral.get_side_lengths(self.point_1, self.point_2, self.point_3, self.point_4)
        return a * b


class Parallelogram(Quadrilateral):

    def checks_parallelogram(self):
        return self.check_sides() and self.check_angle()

    def check_sides(self):
        a, b, c, d = Quadrilateral.get_side_lengths(self.point_1, self.point_2, self.point_3, self.point_4)
        return a == c and d == d

    def check_angle(self):
        return self.get_angle(self.point_1, self.point_2, self.point_4) \
               == self.get_angle(self.point_3, self.point_2, self.point_4) and \
               self.get_angle(self.point_2, self.point_1, self.point_3) \
               == self.get_angle(self.point_4, self.point_1, self.point_3)

    def get_vector(self, point_1, point_2):
        return [point_2[0] - point_1[0], point_2[1] - point_1[1]]

    def get_angle(self, point_1, point_2, point_3):
        vector_1 = self.get_vector(point_1, point_2)
        vector_2 = self.get_vector(point_1, point_3)
        ab = vector_1[0]*vector_2[0] + vector_1[1]*vector_2[1]
        a = sqrt(vector_1[0]**2 + vector_1[1]**2)
        b = sqrt(vector_2[0]**2 + vector_2[1]**2)
        cos_a = ab/(abs(a)*abs(b))
        return round(math.degrees(math.acos(cos_a)))

    def get_area(self):
        pass

    def print(self):
        print(f'Углы {"равны" if self.check_angle() else "не равны"}!')
        print(f'Параллелограмм {"существует" if self.checks_parallelogram() else "не существует"}!')
        # print(self.get_angle(self.point_1, self.point_2, self.point_4))
        # print(self.get_angle(self.point_2, self.point_1, self.point_3))


test = Quadrilateral([0, 0], [0, 5], [5, 5], [5, 0])
test.print()
print("-"*30)
test_2 = Quadrilateral([0, 0], [0, 15], [15, 15], [15, 0])
test_2.print()
print("-"*30)
test_3 = Parallelogram([0, 0], [5, 5], [10, 5], [5, 0])
test_3.print()
print("-"*30)
