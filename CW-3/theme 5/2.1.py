"""2. Написать функцию, вычисляющую площадь прямоугольного параллелепипеда с ребрами a, b и c.
Данная функция должна содержать внутри себе еще одну функцию, вычисляющую площадь прямоугольника.
Решить задачу для случаев, когда общая площадь определена как глобальная и как локальная переменная.
Внести изменения в функции таким образом, чтобы общая площадь могла использоваться как нелокальная переменная."""
s = 0


def func(a, b, c):
    """***"""
    global s

    def square(i, j):
        """***"""
        return i*j

    s = 2*square(a, b) + 2*square(b, c) + 2*square(c, a)


func(2, 4, 6)
print(s)
