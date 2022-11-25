from math import sqrt


class Point:
    number_of_points_y = 0
    number_of_points_x = 0
    number_of_points_zero = 0

    @classmethod
    def inc_count(cls, x, y):
        if Point.on_x(x, y):
            Point.number_of_points_x += 1
        if Point.on_y(x, y):
            Point.number_of_points_y += 1
        if Point.on_zero(x, y):
            Point.number_of_points_zero += 1

    @staticmethod
    def on_x(x, y):
        if x == 0 and y != 0:
            return True

    @staticmethod
    def on_y(x, y):
        if y == 0 and x != 0:
            return True

    @staticmethod
    def on_zero(x, y):
        if x == 0 and y == 0:
            return True

    def __new__(cls, *args, **kwargs):
        print("New point created")
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"Point {x}, {y}")
        self.inc_count(x, y)

    def __del__(self):
        print("Point delete")

    def print_info(self):
        print('*'*20)
        print(f'{self.number_of_points_y}')
        print(f'{self.number_of_points_x}')
        print(f'{self.number_of_points_zero}')

    def move_to_x(self, x):
        self.x += 1

    def move_to_y(self):
        self.y += 1

    def distance_to_origin(self):
        return sqrt((self.x - 0)**2+(self.y - 0)*2)

    def distance_to_point(self, x1, y1):
        return sqrt((x1 - self.x) ** 2 + (y1 - self.y) * 2)

    def coincidence(self, x1, y1):
        if self.x == x1 and self.y == y1:
            return True
        else:
            return False

    def print_point(self):
        print(self.x, self.y)


test_1 = Point(1, 3)
test_1.print_info()

test_2 = Point(10, 0)
test_2.print_info()
print(test_2.distance_to_origin())

test_3 = Point(0, 3)
test_3.print_info()

test_4 = Point(0, 0)
test_4.print_info()
