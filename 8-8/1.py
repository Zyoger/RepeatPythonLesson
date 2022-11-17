import math
from math import sqrt


class Quadrilateral:

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

    @staticmethod
    def get_vector(point_1, point_2):
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
        a, b, c, d = Parallelogram.get_side_lengths(self.point_1, self.point_2, self.point_3, self.point_4)
        return a*d*math.cos(self.get_angle(self.point_1, self.point_2, self.point_4))

    def print(self):
        print(f'Углы {"равны" if self.check_angle() else "не равны"}!')
        print(f'Параллелограмм {"существует" if self.checks_parallelogram() else "не существует"}!')
        print(f"Площадь параллелограмма равна: {self.get_area()}")


"""
Написать программу, демонстрирующую работу с классом: дано N четырехугольников и M параллелограммов, 
найти среднюю площадь N четырехугольников и параллелограммы с наименьшей и наибольшей площадями.
"""
quad_1 = Quadrilateral([0, 0], [0, 5], [5, 5], [5, 0])
quad_2 = Quadrilateral([0, 0], [0, 15], [15, 15], [15, 0])
quad_3 = Quadrilateral([0, 0], [0, 150], [150, 150], [150, 0])
quad_4 = Quadrilateral([0, 0], [0, 25], [25, 25], [25, 0])

parallel_1 = Parallelogram([0, 0], [5, 5], [10, 5], [5, 0])
parallel_2 = Parallelogram([0, 0], [5, 10], [10, 10], [5, 0])
parallel_3 = Parallelogram([0, 0], [5, 15], [10, 15], [5, 0])  # ошибка
parallel_4 = Parallelogram([0, 0], [25, 5], [50, 5], [25, 0])

parallel_1.print()
parallel_2.print()
parallel_3.print()
parallel_4.print()
print(f"Средняя площадь равна: {(quad_1.get_area() + quad_2.get_area() + quad_3.get_area() + quad_4.get_area()/4)}")
print(f"Минимальная площадь: {min(parallel_1.get_area(), parallel_2.get_area(), parallel_3.get_area(), parallel_4.get_area())}")
print(f"Максимальная площадь: {max(parallel_1.get_area(), parallel_2.get_area(), parallel_3.get_area(), parallel_4.get_area())}")

'''
test = Quadrilateral([0, 0], [0, 5], [5, 5], [5, 0])
test.print()
print("-"*30)
test_2 = Quadrilateral([0, 0], [0, 15], [15, 15], [15, 0])
test_2.print()
print("-"*30)
test_3 = Parallelogram([0, 0], [5, 5], [10, 5], [5, 0])
test_3.print()
print("-"*30)
'''
