a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
union = a.union(b)
print(union)
cross = a.intersection(b)
print(cross)
srm = a.symmetric_difference(b)
print(srm)
c = a - cross
print(c)
d = {5, 7, 4}
e = {8, 4, 3}
print(b.issuperset(d))
print(b.issuperset(e))
f = {5, 8, 4, 7, 6}
print(b.issuperset(f))  # неправильно
