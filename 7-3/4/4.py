"""В файле matrix.txt построчно хранится матрица C(k,m). Сформировать вектор D=(d1, d2, d3, …, dk),
 каждый элементы которого представляет собой среднее арифметическое элементов строк матрицы С,
  и вектор G=(g1, g2, g3, …, gm), каждый элемент которого равен количеству отрицательных элементов столбцов матрицы С.
   Записать полученные векторы в соответствующие файлы vectorD.txt и vectorG.txt.
"""
matrix = []
with open("matrix.txt", "r") as file:
    for line in file:
        matrix.append(list(map(int, line.split())))
print(matrix)


def get_average(m):
    result = []
    for i in m:
        result.append(sum(i)/len(i))
    return result


def get_number_of_negative_elements(m):
    result = []
    for i in range(len(m[0])):
        counter = 0
        for j in range(len(m)):
            if m[j][i] < 0:
                counter += 1
        result.append(counter)
    return result


with open("vectorD.txt", "w") as file:
    file.write(f"D = {', '.join(list(map(str, get_average(matrix))))}")


with open("vectorG.txt", "w") as file:
    file.write(f"G = {', '.join(list(map(str, get_number_of_negative_elements(matrix))))}")
