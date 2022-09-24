p = [7, 5, 8, 9, 2, 3, 2, -2, 1, 12, 0]
min_element = sum(p)
counter = 0
for i in p:
    if i >= 0:
        if i < min_element:
            min_element = i

print("Минимальный элемент равен: ", min_element)

for i in p:
    if i == min_element:
        counter += 1

print("Количество вхождений минимального элемента:", counter)
