f = b"nums.dat"
file_open = open(f, "wb")
number = 10
file_open.write(str(number).encode()+b"\n")
for i in range(number):
    file_open.write(str(i).encode()+b" ")
file_open.close()
with open('nums.dat', 'r') as file:
    print(file.read())
