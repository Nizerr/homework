class BankAccount:

    def __init__(self, account_number, balance=0, owner_name=''):
        self.__account_number = account_number
        self.__balance = balance
        self.owner_name = owner_name

    def __str__(self):
        return f"Номер рахунку: {self.__account_number}, Баланс: {self.__balance}"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def account_info(self):
        return f"Номер акаунта: {self.__account_number}, Баланс: {self.__balance}, Власник: {self.owner_name}"

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            recipient.deposit(amount)

    @staticmethod
    def check_account_number(account_number):
        return len(str(account_number)) == 5

    @property
    def get_account_number(self):
        return self.__account_number

    @get_account_number.setter
    def set_account_number(self, new_account):
        if BankAccount.check_account_number(new_account):
            self.__account_number = new_account
        else:
            print("Невірний номер акаунта")

account1 = BankAccount(12345, 1000, "John")
account2 = BankAccount(54321, 500, "Alice")

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

print(account1.get_account_number)
account1.set_account_number = 54321
print(account1.get_account_number)
account1.set_account_number = 1234
