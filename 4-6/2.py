"""
Дана строка. Проверить, сколько слов заканчивается на букву “я”.
"""
text = b"American standard code for information interchange, American standard code for information interchange"
text = text.replace(b',', b'')
text = text.replace(b'.', b' ')
print(text)
s = text.count(b'd ')
print(s)
