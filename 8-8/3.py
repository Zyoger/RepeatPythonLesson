"""Создать класс “Прямоугольник”, свойства - длины сторон, методы - вычисление и вывод сведений о фигуре
- длины сторон, диагонали, периметр, площадь. Создать класс “Треугольник”, свойства - длины сторон, методы -
вычисление и вывод сведений о фигуре - длины сторон, периметр, площадь. Создать производный от них класс
“Прямоугольная пирамида с прямоугольником в основании”, свойства - длины сторон основания и высота, метод
- вычисление объема пирамиды. Написать программу, демонстрирующую работу с классом: дано L прямоугольников,
M треугольников, N прямоугольных пирамид с прямоугольником в основании, найти три прямоугольника с наименьшей
площадью, все прямоугольные треугольники и все пирамиды, объем которых отличается от среднего объема не более,
чем на 10%.
"""
from math import sqrt


class Rectangle:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def print(self):
        print(f"Периметр равен: {self.get_perimetr()}")
        print(f"Площадь равна: {self.get_area()}")
        print(f"Диагональ равна: {self.get_diagonal()}")

    def get_diagonal(self):
        return sqrt(self.a**2 + self.b**2)

    def get_perimetr(self):
        return self.a + self.b + self.c + self.d

    def get_area(self):
        return self.a*self.b


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print(self):
        print(f"Длины сторон: {self.a, self.b, self.c}")
        print(f"Периметр равен: {self.get_perimetr()}")
        print(f"Площадь равна: {self.get_area()}")

    def get_perimetr(self):
        return self.a + self.b + self.c

    def get_area(self):
        p = self.get_semi_perimeter()
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def get_semi_perimeter(self):
        return self.get_perimetr()/2


class RectangularPyramid(Rectangle, Triangle):
    def __init__(self, a, b, c, d, h):
        Rectangle.__init__(self, a, b, c, d)
        Triangle.__init__(self, )

    def get_volume(self):
        pass

    def print(self):
        print(f"Объем равен: {self.get_volume()}")


test_1 = Rectangle(4, 5, 4, 5)
test_1.print()
print('*'*30)
test_2 = Triangle(6, 7, 8)
test_2.print()
print('*'*30)
test_3 = RectangularPyramid(5, 6, 5, 6)
