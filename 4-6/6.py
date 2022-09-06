"""Необходимо декодировать закодированную с помощью кодировки cp866 строку:
"""
code = b'\x8c\xae\xab\xae\xa4\xa5\xe6!\x8e\xe2\xab\xa8\xe7\xad\xa0\xef \xe0\xa0\xa1\xae\xe2\xa0!'
decode = code.decode("cp866")
print(decode)
decode2 = code.decode(errors="ignore")
print(decode2)
