"""
Дан словарь {‘name’: ‘Alex’, ‘age’: 12, ‘class’: ‘v’, ‘roll_id’: ‘2’}.
Проверить принадлежат ли следующие значения  словарю:
‘class’, ‘Alex’, ‘Michael’, ‘4’, 2, ‘2’, ‘age’, ‘address’, (‘name’, ‘Alex’), (‘class’, ‘x’).
"""
s = {"name": "Alex", "age": 12, "class": "v", "roll_id": "2"}
print('class' in s)
print("class" in s.values())
print(s.values())
