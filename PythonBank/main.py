from domain.customer import Customer
from domain.accounts.account import Account
from managers.accountManager import AccountManager
# TODO create account manager class from ac's bank repo

customer1 = Customer('Test', 'User')

# testing the class method
cust_str_1 = 'Sebastian-Coates'
new_cust_1 = Customer.from_string(cust_str_1)
print(Customer.num_of_customers)

manager1 = AccountManager.add_account()



