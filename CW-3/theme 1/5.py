"""5. Написать функцию, которая принимает строку с разделенными дефисом словами и возвращает эту же строку со словами
 отсортированными в алфавитном порядке. Например, строка “green-red-yellow-black-white” должна быть преобразована
  в строку “black-green-red-white-yellow”."""


def new_row(r):
    """***"""
    temp = ''
    row = r.split("-")
    row = sorted(row)
    for word in row:
        temp += word + "-"
    temp = temp.rstrip(temp[-1])
    return print(temp)


line = "green-red-yellow-black-white"
new_row(line)
