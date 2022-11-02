p = {"John": 75, "Ann": 80, "Ally": 60}
p_sort = list(sorted(p.items(), key=lambda item: item[1], reverse=True))
print(p_sort)
p_sort_print = ", ".join(map(lambda item: f"{item[0]} - {item[1]}", p_sort))
print(p_sort_print)

for item in p_sort:
    print(f"{item[0]} - {item[1]}")
