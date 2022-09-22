password = "j5n32esli77"
flag = 0
if (len(password)) >= 5:
    flag += 1

if not password.islower() and not password.isupper():
    flag += 1

if len({"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"} & set(password)) > 0:
    flag += 1

if len({"@", "#", "%", "&"} & set(password)) > 0:
    flag += 1

if flag >= 3:
    print("Пароль подходит")
else:
    print("Пароль не подходит")
    