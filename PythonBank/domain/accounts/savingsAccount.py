from abc import ABC
from account import Account

class SavingsAccount(Account, ABC):

    __total_accounts = 0
    __minimum_balance = 100

    def __init__(self, __account_id, __balance):
        super().__init__(__account_id, __balance)
        SavingsAccount.__total_accounts = +1

    @property
    def account_id(self):
        return self.__account_id

    @property
    def balance(self):
        return self.__balance

    @property
    def total_accounts(self):
        return self.__total_accounts

    @balance.setter
    def balance(self, value):
        self.__balance += value

    def debit(self, value):
        return super(self.can_debit(value)) and (self.__balance() - value) \
               >= self.__minimum_balance


