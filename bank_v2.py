
import os
import json
import requests

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

class BankAccount:
    __exchange_rate = {}

    accounts = []

    @classmethod
    def create_exchange_rate(cls):
        try:
            response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
            data = response.json()
            for currency_data in data:
                currency_code = currency_data["cc"]
                exchange_rate = currency_data["rate"]
                cls.__exchange_rate[currency_code] = exchange_rate
        except Exception as e:
            print(f"Помилка при завантаженні курсів обміну: {e}")

    @classmethod
    def find_accounts_by_owner(cls, owner_name):
        matching_accounts = []
        for account in cls.accounts:
            if account.owner_name == owner_name:
                matching_accounts.append(account)
        return matching_accounts

    @classmethod
    def get_average_balance(cls):
        total_balance = sum(account.balance.amount for account in cls.accounts)
        return total_balance / len(cls.accounts)

    def __init__(self, account_number, balance, owner_name, currency):
        self.account_number = account_number
        self.balance = Money(balance, currency)
        self.owner_name = owner_name
        BankAccount.accounts.append(self)
        self.save_to_file()

    def __str__(self):
        return f"Номер рахунку: {self.account_number}, Баланс: {self.balance}, Власник: {self.owner_name}"

    def deposit(self, amount):
        if amount > 0:
            self.balance.amount += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance.amount:
            self.balance.amount -= amount

    def account_info(self):
        return f"Номер акаунта: {self.account_number}, Баланс: {self.balance}, Власник: {self.owner_name}"

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance.amount:
            self.balance.amount -= amount
            recipient.deposit(amount)

    def transfer_funds(self, target_account, amount):
        if amount > 0 and amount <= self.balance.amount:
            source_currency = self.balance.currency
            target_currency = target_account.balance.currency
            if source_currency == target_currency:
                self.balance.amount -= amount
                target_account.deposit(amount)
            elif source_currency in BankAccount.__exchange_rate and target_currency in BankAccount.__exchange_rate:
                source_rate = BankAccount.__exchange_rate[source_currency]
                target_rate = BankAccount.__exchange_rate[target_currency]
                converted_amount = amount / source_rate * target_rate
                self.balance.amount -= amount
                target_account.deposit(converted_amount)
            else:
                print("Неможливо конвертувати валюту")

    def save_to_file(self):
        filename = f'data/{self.account_number}.json'
        os.makedirs('data', exist_ok=True)
        with open(filename, "w") as file:
            data = {
                "account_number": self.account_number,
                "balance": self.balance.amount,
                "owner_name": self.owner_name,
                "currency": self.balance.currency
            }
            json.dump(data, file, indent=4)

    @staticmethod
    def check_account_number(account_number):
        return len(str(account_number)) == 5



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

