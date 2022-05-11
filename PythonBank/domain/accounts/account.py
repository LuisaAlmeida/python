from abc import ABC, abstractmethod

class Account(ABC):

    def __int__(self, account_id, balance):
        self.__account_id: int = account_id
        self.__balance: int = 0

    @abstractmethod
    def account_id(self) -> int:
        return self.__account_id

    @abstractmethod
    def balance(self) -> int:
        return self.__balance

    @abstractmethod
    def credit(self, amount: int):
        if self.can_credit(amount):
            self.__balance -= amount

    @abstractmethod
    def can_credit(self, amount) -> int:
        return amount > 0

    @abstractmethod
    def debit(self, amount: int):
        if self.can_debit(amount):
            self.__balance -= amount

    @abstractmethod
    def can_debit(self, amount) -> int:
        return 0 < amount <= self.__balance

    @abstractmethod
    def can_withdraw(self):
        return True










