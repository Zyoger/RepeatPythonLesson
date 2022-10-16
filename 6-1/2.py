"""2. Дана последовательность целых чисел. Найти в каждом числе сумму четных цифр."""


def sum_of_even_digits(x):
    """*****"""
    summa = 0
    while x > 0:
        if (x % 10) % 2 == 0:
            summa += x % 10
            x = x // 10
        else:
            x = x // 10
    return summa


subsequence = [1234, 56789, 34567, 98642]
for number in subsequence:
    print(f"Для числа {number} сумма четных цифр: {sum_of_even_digits(number)}")
