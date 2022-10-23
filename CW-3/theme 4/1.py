def func(x):
    """***"""
    result = 0
    if x - 2 >= 0:
        result += x + func(x - 2)
    return result


print(func(10))
