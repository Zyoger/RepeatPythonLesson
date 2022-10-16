line = "aaa(bc[def](ggg(hh)))"
temp = []
dictionary = {")": "(", "]": "[", "}": "{"}
for letter in line:
    if letter in dictionary.values():
        temp.append(letter)
        print(temp)
    elif letter in dictionary.keys():
        if len(temp) == 0 or dictionary[letter] != temp.pop():
            print("Выражение не верно!")
else:
    if len(temp) > 0:
        print("Выражение не верно!")
    else:
        print("Выражение Верно!")

print(temp)
