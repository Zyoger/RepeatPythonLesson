import math


class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def set_number(self, new_a, new_b):
        self.a = new_a
        self.b = new_b

    def get_sum(self):
        return self.a + self.b

    def get_multiplication(self):
        return self.a * self.b


class RightTriangle(Pair):
    def get_hypotenuse(self):
        return math.sqrt(self.a**2 + self.b**2)

    def get_square(self):
        return self.get_multiplication()/2

    def print_info(self):
        print(self.a, self.b)
        print(self.get_hypotenuse())
        print(self.get_square())


test_1 = RightTriangle(4, 5)
test_1.print_info()
