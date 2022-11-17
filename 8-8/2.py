import math
from math import sqrt


class Triangle:

    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def check_existence(self):
        a, b, c = self.get_length_sides()
        angle_a = self.get_angle(self.point_1, self.point_2, self.point_3)
        angle_b = self.get_angle(self.point_2, self.point_1, self.point_3)
        angle_c = self.get_angle(self.point_3, self.point_2, self.point_1)
        print(angle_a, angle_b, angle_c)
        return a+b > c and b+c > a and c+a > b

    def print_info(self):
        print(f"Треугольник {'существует' if self.check_existence() else 'не существует'}!!!")

    def get_length_sides(self):
        a = self.calculate_side(self.point_1, self.point_2)
        b = self.calculate_side(self.point_2, self.point_3)
        c = self.calculate_side(self.point_3, self.point_1)
        return [a, b, c]

    def get_perimetr(self):
        return sum(self.get_length_sides())

    def get_area(self):
        a, b, c = self.get_length_sides()
        angle = self.get_angle(self.point_1, self.point_2, self.point_3)
        return a*b*math.cos(angle)

    @staticmethod
    def calculate_side(point_1, point_2):
        return sqrt((point_2[1] - point_1[1]) ** 2 + (point_2[0] - point_1[0]) ** 2)

    @staticmethod
    def get_vector(point_1, point_2):
        return [point_2[0] - point_1[0], point_2[1] - point_1[1]]

    def get_angle(self, point_1, point_2, point_3):
        vector_1 = self.get_vector(point_1, point_2)
        vector_2 = self.get_vector(point_1, point_3)
        ab = vector_1[0] * vector_2[0] + vector_1[1] * vector_2[1]
        a = sqrt(vector_1[0] ** 2 + vector_1[1] ** 2)
        b = sqrt(vector_2[0] ** 2 + vector_2[1] ** 2)
        cos_a = ab / (abs(a) * abs(b))
        return round(math.degrees(math.acos(cos_a)))


class IsoscelesTriangle(Triangle):
    pass

    def check_existence(self):
        a, b, c = self.get_length_sides()
        return a == b == c

    def print_info(self):
        print(f"Треугольник {'равнобедренный' if self.check_existence() else 'не равнобедренный'}!!!")


test_1 = Triangle([0, 0], [0, 10], [10, 0])
test_1.print_info()
test_2 = Triangle([0, 0], [5, 0], [0, 5])
test_2.print_info()
print("-"*30)
test_3 = IsoscelesTriangle([0, 0], [5, 5*sqrt(3)], [10, 0])
test_3.print_info()
