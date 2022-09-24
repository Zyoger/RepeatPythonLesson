for i in range(5, 26):
    if i % 3 == 0 or i % 6 == 0:
        continue
    if i % 5 == 0:
        print(i, "кратно 5")
        continue
    print(i)
