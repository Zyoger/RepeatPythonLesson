numbers = [1, 21, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number % 2 == 0:
        print(number)
        break
else:
    print("Четных чисел нет!")
