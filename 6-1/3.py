"""3. Дана последовательность целых чисел. Для каждого числа последовательности проверить, представляют ли его цифры
 строго возрастающую последовательность."""


def subsequence(x):
    """*****"""
    flag = True
    while x >= 0:
        if x >= 10:
            if x % 10 > (x // 10) % 10:
                x = x // 10
            else:
                flag = False
                break
        else:
            break
    return flag


p = [12345, 56789, 98765, 12342, 45367]
for num in p:
    print(subsequence(num))

