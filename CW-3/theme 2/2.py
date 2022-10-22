"""2. Написать функцию, которая принимает произвольное число чисел и преобразовывает их таким образом, чтобы цифры
 каждого числа (по умолчанию) были записаны в обратном порядке. Предусмотреть возможность по запросу пользователя
  выполнять преобразования только над нечетными числами."""


def change(x):
    """***"""
    temp = []
    result = 0
    while x != 0:
        temp.append(x % 10)
        x = x // 10
    for i in range(0, len(temp)):
        result += temp[i] * 10**(len(temp) - (i+1))
    return result


p = [123, 345, 567, 78, 1234]


def func(line, mode=False):
    """***"""
    new_line = []
    for elem in line:
        if mode:
            if not even_or_not(elem):
                new_line.append(change(elem))
        else:
            new_line.append(change(elem))
    return new_line


def even_or_not(c):
    """***"""
    if c % 2 == 0:
        return True
    else:
        return False


print(func(p, mode=True))
print(func(p, mode=False))
