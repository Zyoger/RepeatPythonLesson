"""2. Дан некоторый текст. Определить количество вхождений в него каждого символа."""
line = "Пример текста для задачи"
letters = list(set(line))
print(letters)
for i in range(len(letters)):
    print(f"Символ '{letters[i]}' - {line.count(letters[i])}")
