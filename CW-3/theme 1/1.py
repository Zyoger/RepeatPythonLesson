"""1. Дана последовательность из N целых чисел. Сформировать последовательность, каждый элемент которой равен сумме
 цифр соответствующего элемента исходной последовательности. Найти сумму цифр в сформированной последовательности."""

subsequence = [12, 13, 14, 15, 16, 17, 18]


def get_sum_digits(digit):
    """Возвращает сумму цифр."""
    sum_digits = 0
    while digit != 0:
        sum_digits += digit % 10
        digit = digit // 10
    return sum_digits


def create_new_subsequence(sub):
    """Создает новую последовательность."""
    new_subsequence = []
    for digit in sub:
        new_subsequence.append(get_sum_digits(digit))
    return new_subsequence


def get_sum_digit_subsequence(subs):
    """Возвращает сумму всех цифр в последовательности."""
    sum_subsequence = 0
    for digit in subs:
        sum_subsequence += digit
    return sum_subsequence


print(create_new_subsequence(subsequence))
print(get_sum_digit_subsequence(create_new_subsequence(subsequence)))
