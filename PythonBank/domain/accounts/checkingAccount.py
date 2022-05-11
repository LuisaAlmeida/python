from abc import ABC
from account import Account

class CheckingAccount(Account, ABC):

    __total_accounts: int = 0

    def __init__(self, __account_id, __balance):
        super().__init__(__account_id, __balance)
        CheckingAccount.__total_accounts += 1

    @property
    def account_id(self) -> int:
        return self.__account_id

    @classmethod
    def total_accounts(cls) -> int:
        return cls.__total_accounts

