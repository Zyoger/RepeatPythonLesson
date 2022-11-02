class Straight:
    x1, y1 = 3, 2
    x2, y2 = 0, 6

    def print(self):
        a = self.y2 - self.y1
        b = self.x1 - self.x2
        c = self.x2 * self.y1 - self.x1 * self.y2
        print(f"Уравнение прямой имеет вид: {a:-}x{b:+}y{c:+}=0")

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
a.print()
print(a.get_intersection_points())
