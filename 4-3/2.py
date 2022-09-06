import math


def square(r):
    s = math.pi*r**2
    return s


def length(r):
    l = 2*math.pi*r
    return l


a = 10
print(f"Площадь окружности: {square(a)}")
print(f"Длина окружности: {length(a)}")
a = 15
print(f"Площадь окружности: {square(a)}")
print(f"Длина окружности: {length(a)}")

