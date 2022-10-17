"""5. Дано натуральное число N. Уменьшить число в 2 раза (деление нацело) и проверить, изменилось ли после уменьшения
 количество разрядов в числе."""


def divider(x):
    """*****"""
    if number_digits(x // 2) != number_digits(x):
        return True
    else:
        return False


def number_digits(x):
    """*****"""
    counter = 0
    while x > 0:
        counter += 1
        x = x // 10
    return counter


print(divider(101))
