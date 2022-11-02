class Straight:
    count_parallel = 0
    count_cross_zero = 0

    def set(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def print(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        a = y2 - y1
        b = x1 - x2
        c = x2 * y1 - x1 * y2
        print(f"Уравнение прямой имеет вид: {a:-}x{b:+}y{c:+}=0")
        if c == 0:
            Straight.count_cross_zero += 1
        if x1 == x2 or y1 == y2:
            Straight.count_parallel += 1

    def get_intersection_points(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
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
        point = [x, y]
        return point


a = Straight()
a.set(3, 2, 0, 6)
a.print()
print(a.get_intersection_points())
print(Straight.count_parallel)
print(Straight.count_cross_zero)
