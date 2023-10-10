from bank_v3 import NewBankAccount
from bank_v2 import BankAccount

class UpBankAccount(BankAccount):

    def __init__(self, account_number, balance, owner_name, currency, max_limit, max_count_transactions):
        super().__init__(account_number, balance, owner_name, currency)
        self.max_limit = max_limit
        self.max_count_transactions = max_count_transactions
        self.currency = currency

    def __eq__(self, other):
        return self.currency == other.currency

    def convertation_to_uah(self, amount):
        if self.currency == "USD":
            return amount * BankAccount._BankAccount__exchange_rate.get("USD", 1)
        elif self.currency == "EUR":
            return amount * BankAccount._BankAccount__exchange_rate.get("EUR", 1)
        else:
            return amount

    def __lt__(self, other):
        return self.balance.amount < (other.balance.amount if self.currency == other.currency else self.convertation_to_uah(other.balance.amount))

    def __le__(self, other):
        return self.balance.amount <= (other.balance.amount if self.currency == other.currency else self.convertation_to_uah(other.balance.amount))

    def __gt__(self, other):
        return self.balance.amount > (other.balance.amount if self.currency == other.currency else self.convertation_to_uah(other.balance.amount))

    def __ge__(self, other):
        return self.balance.amount >= (other.balance.amount if self.currency == other.currency else self.convertation_to_uah(other.balance.amount))

    def __bool__(self):
        return self.balance.amount > 0

    def __add__(self, numb):
        self.balance.amount += numb
        return self

    def __sub__(self, numb):
        self.balance.amount -= numb
        return self

    def __call__(self, value=0):
        if value < 0:
            print(f"Знято {abs(value)} {self.currency}")
            self.balance.amount -= abs(value)
        elif value > 0:
            print(f"Поповнено {value} {self.currency}")
            self.balance.amount += value
        else:
            print(f"Баланс: {self.balance.amount} {self.currency}")

    def __setattr__(self, name, value):
        if name == "balance":
            print(f"Змінено баланс: було {self.__dict__.get(name, 0)}, стало {value}")
            self.__dict__[name] = value
        else:
            object.__setattr__(self, name, value)


if __name__ == "__main__":
    BankAccount.create_exchange_rate()

    account1 = NewBankAccount(12345, 1000, "John", "USD", 500, 5)
    account2 = UpBankAccount(54321, 500, "Alice", "EUR", 300, 3)

    print(account1)
    print(account2)

    account1.deposit(200)
    account2.withdraw(100)

    print(account1.account_info())
    print(account2.account_info())

    account1.transfer(account2, 300)

    print(account1.account_info())
    print(account2.account_info())

    print(account1 == account2)

    print(account1 < account2)
    print(account1 <= account2)
    print(account1 > account2)
    print(account1 >= account2)

    print(bool(account1))
    print(bool(account2))

    account1 + 100
    account2 - 50

    print(account1.account_info())
    print(account2.account_info())

    account1.balance.amount = 1500
    print(account1.balance.amount)
