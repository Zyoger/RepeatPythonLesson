"""
Даны три пересекающихся множества A, B и C. Проверьте справедливость равенства: (A - B) - C = (A - C) - (B - C).
Подтвердите полученный результат с помощью кругов Эйлера.
"""
A = {1, 2, 3, 4, 5, 6}
B = {3, 4, 5, 6, 7, 8, 9}
C = {6, 7, 8, 9, 10, 11}
print((A - B) - C == (A - C) - (B - C))
