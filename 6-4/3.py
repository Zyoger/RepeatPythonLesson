"""3. Написать рекурсивную функцию подсчета суммы первых n членов гармонического ряда: """


def summa(x):
    """*****"""
    if x == 1:
        return x
    return 1 / x + summa(x - 1)


print(summa(5))
