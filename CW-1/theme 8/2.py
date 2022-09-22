d = {'smart watch': 550, 'phone': 1000, 'playstation': 500, 'laptop': 1550, 'music player': 600, 'tablet': 400}
print(sum(d.values()))
all = (list(d.keys()))
print(all)
print(sorted(all))
print(sorted(all, reverse=True))
d["music player"] /= 2
print(d)
summ_sell_nout_and_phone = 5*d["phone"] + 3*d["laptop"]
print(summ_sell_nout_and_phone)
price_tablet = d["tablet"]
print(price_tablet)
flag = 1
while summ_sell_nout_and_phone > price_tablet:
    price_tablet += d["tablet"]
    flag += 1
print(flag)
prise = d.popitem()
print(prise)
print(d)
prise = d.popitem()
print(prise)
print(d)
d.setdefault("iphone", 1300)
d.setdefault("music player", 850)
d.setdefault("headphones", 200)
print(d)

