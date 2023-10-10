from bank_v2 import BankAccount

class NewBankAccount(BankAccount):
    def __init__(self, account_number, balance, owner_name, currency, max_limit, max_count_transactions):
        super().__init__(account_number, balance, owner_name, currency)
        self.max_limit = max_limit
        self.max_count_transactions = max_count_transactions
        self.currency = currency

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance.amount and amount <= self.max_limit:
            self.balance.amount -= amount
            self.max_count_transactions -= 1

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance.amount and amount <= self.max_limit:
            super().transfer(recipient, amount)
            self.max_count_transactions -= 1

    def add_interest(self, percentage):
        if percentage > 0:
            interest = self.balance.amount * (percentage / 100)
            self.balance.amount += interest

    def __add__(self, numb):  # Define the __add__ method
        if numb > 0:
            self.balance.amount += numb
        return self

BankAccount.create_exchange_rate()

account1 = NewBankAccount(12345, 1000, "John", "USD", 500, 5)
account2 = NewBankAccount(54321, 500, "Alice", "EUR", 300, 3)

if __name__ == "__main__":
    BankAccount.create_exchange_rate()

    account1 = NewBankAccount(12345, 1000, "John", "USD", 500, 5)
    account2 = NewBankAccount(54321, 500, "Alice", "EUR", 300, 3)

    print(account1)
    print(account2)

    account1.deposit(200)
    account2.withdraw(100)

    print(account1.account_info())
    print(account2.account_info())

    account1.transfer(account2, 300)

    print(account1.account_info())
    print(account2.account_info())

    print(BankAccount.check_account_number(12345))
    print(BankAccount.check_account_number(1234))

    print(account1.get_average_balance())
    print(account2.get_average_balance())

    matching_accounts = BankAccount.find_accounts_by_owner("John")
    for account in matching_accounts:
        print(account.account_info())

    account1.add_interest(15)
    account2.add_interest(10)

    account1.transfer_funds(account2, 500)
    print(account1.account_info())
    print(account2.account_info())
