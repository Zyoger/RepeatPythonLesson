a = 5
print(type(a))
print(id(a))
b = 12
print(type(b))
print(id(b))
c = 5.7
print(type(c))
print(id(c))
a = 12
print(id(a))
a = c
print(id(c))
d = e = f = 125
print(id(d) == id(e) == id(f))
