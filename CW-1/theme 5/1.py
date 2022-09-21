password = "P5n32esli77@"
print((len(password)) >= 5)
print(not password.islower() and not password.isupper())
print(len({"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"} & set(password)) > 0)
print(len({"@", "#", "%", "&"} & set(password)) > 0)

