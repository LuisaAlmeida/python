from abc import ABC, abstractmethod

class Account(ABC):

    def __int__(self, account_id, balance):
        self.__account_id = account_id
        self.__balance = 0

    @abstractmethod
    def account_id(self):
        return self.__account_id

    @abstractmethod
    def balance(self):
        return self.__balance

    @abstractmethod
    def credit(self, amount):
        if self.can_credit(amount):
            self.__balance -= amount

    @abstractmethod
    def can_credit(self, amount):
        return amount > 0

    @abstractmethod
    def debit(self, amount):
        if self.can_debit(amount):
            self.__balance -= amount

    @abstractmethod
    def can_debit(self, amount):
        return 0 < amount <= self.__balance

    @abstractmethod
    def can_withdraw(self):
        return True










