"""3. Найти 2-ое, 6-ое и 11-ое по счету числа кратные 7, но не кратные 13 в диапазоне от 1000 до 2000"""
counter = 0
for i in range(1000, 2001):
    if i % 7 == 0 and i % 13 != 0:
        counter += 1
    else:
        continue
    if counter == 2 or counter == 6 or counter == 11:
        print(i)
