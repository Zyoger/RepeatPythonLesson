"""5. Дан список игроков команды, причем для каждого игрока указаны его имя, фамилия и игровой рейтинг
 (по шкале от 1 до 10, где 10 - наивысший балл). Отсортируйте список игроков по фамилии,
  а затем по их рейтингу от лучшего к худшему и наоборот. Решите задачу с использованием lambda-функций."""
players = [{'name': 'Antony', 'last name': 'Bloom', 'raiting': 9},
           {'name': 'Alon', 'last name': 'Riddler', 'raiting': 10},
           {'name': 'Greg', 'last name': 'Mc Queen', 'raiting': 4},
           {'name': 'Michael', 'last name': 'Anders', 'raiting': 6}]

sorted_players = list(sorted(players, key=lambda i: i["last name"]))
print(sorted_players)
sorted_players = list(sorted(players, key=lambda i: i["raiting"], reverse=True))
print(sorted_players)
sorted_players = list(sorted(players, key=lambda i: i["raiting"]))
print(sorted_players)
