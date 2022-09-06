"""
Дано несколько чисел: 543731, 4472, 999999, 347623 и 1000001. Найти для каждого числа количество уникальных цифр,
которое оно содержит, а также минимальную и максимальную цифру.
"""
a = "543731"
b = "4472"
c = "999999"
d = "347623"
e = "1000001"
s = sorted(set(a).union(set(b), set(c), set(d), set(e)))
print(s)

print(len(set(a) - set(b) - set(c) - set(d) - set(e)))
print(len(set(b) - set(a) - set(c) - set(d) - set(e)))
print(len(set(c) - set(b) - set(a) - set(d) - set(e)))
print(len(set(d) - set(b) - set(c) - set(a) - set(e)))
print(len(set(e) - set(b) - set(c) - set(d) - set(a)))
print(min(set(a)), max(set(a)))
print(min(set(b)), max(set(b)))
print(min(set(c)), max(set(c)))
print(min(set(d)), max(set(d)))
print(min(set(e)), max(set(e)))