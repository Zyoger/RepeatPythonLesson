"""4. Дан диапазон целых чисел от n1 до n2. Найти факториал каждого третьего простого числа в заданном диапазоне. """


def prime_number(x):
    """*****"""
    for divider in range(2, x-1):
        if x % divider == 0:
            return False
    return True


def factorial(x):
    """*****"""
    res = 1
    for num in range(2, x+1):
        res *= num
    return res


i = 4
j = 11
count = 0
for number in range(i, j+1):
    if prime_number(number):
        count += 1
        if count % 3 == 0:
            print(factorial(number))
