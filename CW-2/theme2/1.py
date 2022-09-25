n = 691554
max = 0
temp = 0
position = len(str(n))
for i in range(0, len(str(n))):
    temp = n % 10
    n = n // 10
    if max < temp:
        max = temp
        position = len(str(n))

print(max)
print(position)
