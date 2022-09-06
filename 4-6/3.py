"""
Дана строка. Подсчитать количество букв “т” в строке.
"""
text = b"American standard code for information interchange, American standard code for information interchange"
text.replace(b'.', b' ')
text.replace(b',', b'')
s = text.count(b's')
print(s)