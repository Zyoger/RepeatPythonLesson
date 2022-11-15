from math import sqrt


class Quadrilateral:
    # [x, y]
    point_1 = [0, 0]
    point_2 = [0, 0]
    point_3 = [0, 0]
    point_4 = [0, 0]

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
        status = "Прямоугольник существует!" if self.checks_existence() else "Прямоугольник не существует!"
        print(status)
        print(f"Длины сторон: {Quadrilateral.get_side_lengths(self.point_1, self.point_2, self.point_3, self.point_4)}")
        print(f"Периметр равен: {self.get_perimetr()}")
        print(f"Площадь равна: {self.get_area()}")
        print(f"Диагональ равна: {self.get_diagonal()}")

    @staticmethod
    def get_side_lengths(point_1, point_2, point_3, point_4):
        a = point_2[1] - point_1[1]
        b = point_3[0] - point_2[0]
        c = point_3[1] - point_4[1]
        d = point_4[0] - point_1[0]
        return [a, b, c, d]

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
    pass


test = Quadrilateral([0, 0], [0, 5], [5, 5], [5, 0])
test.print()
print("-"*30)
test_2 = Quadrilateral([0, 0], [0, 15], [15, 15], [15, 0])
test_2.print()
