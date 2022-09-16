import math
a = 18
b = 3
i = 8
y = math.pow(((1+a+math.sqrt(a))/(2*a+math.sqrt(a))+2-(1-a+math.sqrt(a))/(2*a-math.sqrt(a))), -1) * (5-2*math.sqrt(a))
print(y)

a = math.radians(a)
b = math.radians(b)
i = math.radians(i)
y = 1/4*(math.sin(a+b-i)+math.sin(b+i-a))+math.sin(i+a-b)-math.sin(a+b+i)
print(y)
