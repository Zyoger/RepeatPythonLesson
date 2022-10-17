"""1. Напишите программу, осуществляющую проверку логина и пароля для входа в систему. Проверка введенных пользователем
 данных должна осуществляться в отдельной функции, принимающей следующие параметры: имя пользователя, пароль,
  количество попыток входа в систему (по умолчанию 3), сообщение, выводимое пользователю в случае, если все
   попытки входа в систему исчерпаны (по умолчанию: “Система заблокирована. Повторите попытку через 5 мин.”)"""
base = {"egor": "12345", "anna": "12345", "maya": "12345"}


def password_check(name, password, attempts=3, message="Система заблокирована. Повторите попытку через 5 мин."):
    """*****"""
    for attempts in reversed(range(attempts + 1)):
        if name in base.keys() and password == base[name]:
            return print("Доступ получен!")
        else:
            if attempts > 0:
                name = input("Имя: ")
                password = input("Пароль: ")
                if name in base.keys() and password == base[name]:
                    return print("Доступ получен!")
            if attempts == 0:
                return print(message)


password_check("egor", "1234")
