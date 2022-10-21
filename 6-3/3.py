"""3. Напишите программу, которая будет считать количество четных и нечетных чисел в заданном списке с помощью
 lambda-функции."""

list_of_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1 option
even = list(filter(lambda i: i % 2 == 0, list_of_number))
not_even = list(filter(lambda i: i % 2 != 0, list_of_number))
print(f"Even: {len(even)}, not even: {len(not_even)}")
# 2 option
map_list = list(map(lambda j: j % 2, list_of_number))
print(map_list.count(0), map_list.count(1))
