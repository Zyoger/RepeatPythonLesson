"""3. Напишите функцию, которая может принимать произвольное количество аргументов (целых чисел), и определять,
сколько среди них двузначных и трёхзначных чисел. Определение количества разрядов в числе также оформить в виде
 отдельной функции."""


def rank_in_number(x):
    """*****"""
    counter = 1
    while x >= 10:
        counter += 1
        x = x // 10
    return counter


def counter_of_rank(*args):
    """*****"""
    two = 0
    tree = 0
    for i in args:
        if rank_in_number(i) == 2:
            two += 1
        elif rank_in_number(i) == 3:
            tree += 1
    return print(f"Tho = {two}, Tree = {tree}")


counter_of_rank(12, 34, 23, 45, 234, 345, 456, 5676)
