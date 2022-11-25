class Account:
    rub_euro = 0.0156
    rub_dollar = 0.0166

    def __new__(cls, *args, **kwargs):
        print("Bank account created")
        return super().__new__(cls)

    def __init__(self, surname, account_number, accrual_percentage, amount_in_rubles):
        self.__amount_in_rubles = amount_in_rubles
        self.__accrual_percentage = accrual_percentage
        self.__account_number = account_number
        self.__surname = surname
        print("Bank account opened")

    def __del__(self):
        print("Bank account closed!!!")

    @staticmethod
    def exchange_to(amount, exchange_rate):
        return amount*exchange_rate

    @classmethod
    def edit_ruble_exchange_rate_to_euros(cls, new_xchange_rate):
        Account.rub_euro = new_xchange_rate

    @classmethod
    def edit_ruble_exchange_rate_to_dollars(cls, new_xchange_rate):
        Account.rub_dollar = new_xchange_rate

    def change_of_account_owner(self, new_account_owner):
        self.__surname = new_account_owner

    def withdrawal_of_a_specified_amount(self, withdrawal):
        self.__amount_in_rubles -= withdrawal

    def accrual_of_a_specified_amount(self, accrual):
        self.__amount_in_rubles += accrual

    def accrual_of_interest(self):
        self.__amount_in_rubles += self.__amount_in_rubles * self.__accrual_percentage

    def transfer_to_dollars_do_not_accept_parameters(self):
        pass

    def transfer_to_euros_do_not_accept_parameters(self):
        pass

    def get_info(self):
        print(self.__surname)
        print("*" * 30)
        print(self.__account_number)
        print(self.__amount_in_rubles)
        print(self.__accrual_percentage)
        print("*" * 30)


account_123456 = Account("Tarakanov", 987654, 0.03, 9999)
account_123456.get_info()
account_123456.accrual_of_a_specified_amount(1000)
account_123456.get_info()
account_123456.withdrawal_of_a_specified_amount(2000)
account_123456.get_info()
account_123456.accrual_of_interest()
account_123456.get_info()
