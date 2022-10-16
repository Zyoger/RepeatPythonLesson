"""1. Дана последовательность целых чисел. Для каждого числа последовательности найти количество его делителей."""


def the_number_of_divisors(x):
    """*****"""
    number = 0
    for divisor in range(1, x+1):
        if x % divisor == 0:
            number += 1
    return number


subsequence = [1, 2, 3, 4, 5, 6, 7, 10, 12, 15, 32, 64]
for elem in subsequence:
    print(f"Для числа {elem} есть {the_number_of_divisors(elem)} делителей.")
