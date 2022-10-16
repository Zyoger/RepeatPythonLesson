goods = {"milk": 12, "bread": 10, "meat": 60, "vegetablemix": 20, "fruitmix": 35, "fish": 45, "eggs": 15, "cake": 15}
total_money = 100
total_cost = 0
for key in goods.keys():
    if total_cost >= total_money:
        print("Деньги кончились!")
        break
    else:
        total_cost += goods[key]
        print(key)
else:
    print("Денег хватило на все!")
