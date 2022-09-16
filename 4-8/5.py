"""
Дан словарь {‘gold’: 500, ‘pouch’: [‘flint’, ‘twine’, ‘gemstone’], ‘backpack’: [‘xylophone’, ‘dagger’, ‘bedroll’,
 ‘bread loaf’]}. Добавьте в словарь еще один элемент ‘pocket’, содержащий следующие значения: ‘seashell’,
  ‘strange berry’, ‘lint’. Отсортируйте значения, принадлежащие ключу ‘backpack’ и затем удалите из них значение
   ‘dagger’. Увеличьте  на 50 значение, принадлежащее ключу ‘gold’.
"""
s = {"gold": 500, "pouch": ["flint", "twine", "gemstone"], "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]}
s.setdefault("pocket", ["seashell", "strange berry", "lint"])
print(s)
a = sorted(s.pop("backpack"))
print(a)
a.remove("dagger")
s.setdefault("backpack", a)
print(s)
b = s.pop("gold")
print(b)
b += 50
print(b)
s.setdefault("gold", b)
print(s)
