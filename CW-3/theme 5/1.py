"""1. Напишите функцию, ведущую подсчет количества посещений указанного города. Функция должна принимать в качестве
 аргумента название города и возвращать некоторую внутреннюю функцию, которая каждый раз при ее вызове будет
  увеличивать счетчик посещений на 1. При решении задачи используйте нелокальную область видимости."""


def func(city):
    """***"""
    counter = 0

    def inc():
        """***"""
        nonlocal counter
        counter += 1
        return print(city, counter)

    return inc


f1 = func("Moscow")
f1()
f1()
f2 = func("Yarik")
f2()
f2()

