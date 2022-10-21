"""1. Написать рекурсивную функцию подсчета суммы элементов списка чисел."""


def summa(x):
    """*****"""
    if len(x) == 1:
        return x[0]
    return summa(x[1:]) + x[0]


list_of_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(summa(list_of_number))
