class Straight:
    count_parallel = 0
    count_cross_zero = 0

    def __new__(cls, *args, **kwargs):
        print("Это конструктор!!!")
        return super().__new__(cls)

    def __init__(self, x1, y1, x2, y2):
        print("Это инициализатор!!!")
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def __del__(self):
        print("Это деструктор!!!")

    @classmethod
    def inc_count(cls, zero, parallel):
        if zero:
            cls.count_cross_zero += 1
        if parallel:
            cls.count_parallel += 1

    def print(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        a = y2 - y1
        b = x1 - x2
        c = x2 * y1 - x1 * y2
        print(f"Уравнение прямой имеет вид: {a:-}x{b:+}y{c:+}=0")
        Straight.inc_count(c == 0, x1 == x2 or y1 == y2)
        point = Straight.get_intersection_points(x1, x2, y1, y2)
        print(f'Точки пересечения прямой с осями координат: ({round(point[0])}:0), (0:{round(point[1])})')

    @staticmethod
    def get_intersection_points(x1, x2, y1, y2):
        x = None
        y = None
        if (x1 != x2) and (y1 != y2):
            x = -(x2 * y1 - x1 * y2) / (y2 - y1)  # пересечение с "х"
            y = -(x2 * y1 - x1 * y2) / (x1 - x2)  # пересечение с "Y"
        elif x1 == x2:
            x = x1
            y = 0
        elif y1 == y2:
            y = y1
            x = 0
        return [x, y]


a = Straight(3, 2, 0, 6)
a.print()
print(Straight.count_parallel)
print(Straight.count_cross_zero)
