"""2. Вывести на экран последовательность из первых 100 простых чисел. Найти сумму элементов полученной
 последовательности."""


def get_subsequence(n):
    """Возвращает новую последовательность из N чисел."""
    new_subsequence = []
    counter = 0
    start_number = 2
    while counter <= n:
        if prime_number(start_number):
            new_subsequence.append(start_number)
            counter += 1
            start_number += 1
        else:
            start_number += 1
    return new_subsequence


def prime_number(digit):
    """Возвращает True если число простое."""
    if digit == 2:
        return True
    else:
        for i in range(2, digit):
            if digit % i == 0:
                return False
        return True


def sum_subsequence(subsequence):
    """Возвращает сумму последовательности."""
    sum_sub = 0
    for digit in subsequence:
        sum_sub += digit
    return sum_sub


print(get_subsequence(15))
print(sum_subsequence(get_subsequence(15)))
