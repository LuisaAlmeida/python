
class Customer:

    num_of_customers: int = 0

    def __init__(self, first, last):
        self.__first: str = first
        self.__last: str = last
        Customer.num_of_customers += 1

    # class methods are Alternative Constructors, in this case: from a string divided by '-'
    @classmethod
    def from_string(cls, cust_str):
        first, last = cust_str.split('-')
        return cls(first, last)

    @property
    def first(self) -> str:
        return self.__first

    @first.setter
    def first(self, value: str):
        self.__first = value

    @property
    def last(self) -> str:
        return self.__last

    @last.setter
    def last(self, value: str):
        self.__last = value

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @full_name.setter
    def full_name(self, value: str):
        first, last = value.split(' ')
        self.__first = first
        self.__last = last

    @full_name.deleter
    def full_name(self):
        self.__first = None
        self.__last = None
        print('Names Deleted')

    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)
