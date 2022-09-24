name = input("Name: ")
password = input("Password: ")

while True:
    if len(password) >= 8 and not password.count(name):
        print("Ok")
        break
    password = input("Return password: ")
