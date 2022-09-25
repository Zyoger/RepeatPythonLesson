x = 0
y = 0

if x == 0 and y == 0:
    print("Начало координат")
elif x == 0 or y == 0:
    print("Лежит на оси")
elif x > 0 and y > 0:
    print("1")
elif x < 0 and y < 0:
    print("3")
elif x < 0 and y > 0:
    print("2")
elif x > 0 and y < 0:
    print("4")
