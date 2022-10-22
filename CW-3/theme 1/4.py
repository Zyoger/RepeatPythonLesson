"""4. Написать функцию, которая выводит на экран первые N строк треугольника Паскаля. *Треугольник Паскаля
 - это бесконечная таблица чисел, имеющая форму треугольника, в котором на вершине и по бокам стоят единицы,
  а каждый центральный элемент равен сумме двух элементов, расположенных над ним."""


def pascal(n):
    """*****"""
    current_row = [1]
    for i in range(1, n+1):
        print(" "*(n-i), current_row)
        current_row = get_row(current_row)


def get_row(old_row):
    """*****"""
    new_row = [1]
    for i in range(0, len(old_row)-1):
        new_row.append(old_row[i]+old_row[i+1])
    new_row.append(1)
    return new_row


pascal(1)
