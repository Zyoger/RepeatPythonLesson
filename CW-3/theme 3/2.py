"""2. Дан список имен. Найдите сумму длин имен списка после удаления всех имен, начинающихся с маленькой буквы.
Решите задачу с использованием lambda-функций."""

line = ["Egor", "Anna", "Maya", "goga", "sasha"]
line = list(filter(lambda i: i[0].isupper(), line))
print(line)
line = list(map(lambda i: len(i), line))
print(line)
print(sum(line))
