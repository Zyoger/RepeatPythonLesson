"""2. Написать рекурсивную функцию, вычисляющую сумму элементов списка, элементы которого также могут быть списком.
 Например, для списка [1, 2, [3, 4], [5, 6]] сумма элементов равна 21."""
line = [1, 2, [3, 4], [5, 6]]


def func(x):
    """***"""
    result = 0
    for elem in x:
        if type(elem) is list:
            result += func(elem)
        else:
            result += elem
    return result


print(func(line))
