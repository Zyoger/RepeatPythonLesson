password = "P5n32esli77@"
flag1 = (len(password)) >= 5
flag2 = not password.islower() and not password.isupper()
flag3 = len({"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"} & set(password)) > 0
flag4 = len({"@", "#", "%", "&"} & set(password)) > 0
if flag1 and flag2 and flag3 and flag4:
    print("Пароль подходит")
else:
    print("Пароль не подходит")
