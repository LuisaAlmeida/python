from domain.customer import Customer
from managers.accountManager import AccountManager

class Bank:

    __total_customers: int = 0
    __total_accounts: int = 0

    def __init__(self, bank_name, customer: [Customer]):
        self.__bank_name: str = bank_name
        self.__customer: Customer = customer
        self.__account_manager: AccountManager = AccountManager()
        Bank.__total_customers += 1

    @classmethod
    def total_customer(cls):
        return cls.__total_customers

    @property
    def bank_name(self):
        return self.__bank_name

    @bank_name.setter
    def bank_name(self, value):
        self.__bank_name = value




