"""
Определите, сколько раз в тексте встречается заданное слово
(взять произвольный текст и проверить решение для 2-3 разных слов).
"""
text = b"American standard code for information interchange, American standard code for information interchange"
print(text.count(b"standard"))
print(text.count(b"information"))
print(text.count(b"code"))