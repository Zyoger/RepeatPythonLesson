name = input("Name: ")
password = input("Password: ")
counter = 0

while counter < 2:
    if len(password) >= 8 and not password.count(name):
        print("Ok")
        break
    password = input("Return password: ")
    counter += 1
else:
    print("Пароль за три попытки пароль так и не был установлен!!!")
