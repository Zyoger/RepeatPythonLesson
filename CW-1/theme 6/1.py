s = b"restart"
firststring = s[0:1]
print(firststring)
s = firststring + s[1:].replace(b"r", b"$", 1)
print(s)
