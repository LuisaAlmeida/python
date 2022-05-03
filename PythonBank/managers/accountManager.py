from domain.accounts.account import Account

class AccountManager:

    __number_accounts = 0

    # self.__accounts_map = {i: accounts_map[i] for i in range(0, len(accounts_map))}
    def __int__(self, accounts=None):
        if accounts is None:
            accounts = [Account]
            self.__number_accounts += 1
        if accounts is None:
            self.accounts = []
        else:
            self.accounts = accounts

    @staticmethod
    def add_account(self, new_account):
        if new_account not in self.accounts:
            self.accounts.append(new_account)
            self.__number_acounts += 1
            print('The account has been added')

    @staticmethod
    def remove_account(self, acc):
        if acc is self.accounts:
            self.accounts.remoce(acc)
            self.__number_acounts -= 1
            print('The account has been deleted')

    @staticmethod
    def print_accounts(self):
        for acc in self.accounts:
            print('--> ', acc.account_id())

    @staticmethod
    def deposit(self, amount):
        self.accounts() + amount
        print('You have successfully deposited this ' + amount)

    @staticmethod
    def withdraw(self, acc, amount):
        if acc not in self.accounts:
            print('You do not have an account')
            return
        if acc is self.accounts:
            if acc.can_withdraw():
                acc.balance() - amount
                print('You have withdraw ' + amount)

    @staticmethod
    def transfer(self, src_id, dst_id, amount):
        src_account = self.accounts.account_id(src_id)
        dst_account = self.accounts.account_id(dst_id)
        if src_account.can_debit(amount) and dst_account.can_credit(amount):
            src_account.debit(amount)
            dst_account.credit(amount)
            print('Your transfer was successful')
