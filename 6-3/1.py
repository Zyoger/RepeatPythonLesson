"""1. Используя функцию sorted() и lambda-функцию, отсортируйте список кортежей по последнему символу их
второго элемента."""

m = [('Магазин', 'railway_fork'), ('Игры', 'games'), ('Информация о боте', 'menu_item'), ('Пополнить счет', 'info')]

print(list(sorted(m, key=lambda elem: elem[1])))

