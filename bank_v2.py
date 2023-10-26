
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

    def __init__(self, account_number, balance, owner_name, currency, daily_limit, interest_rate):
        self.account_number = account_number
        self.balance = Money(balance, currency)
        self.owner_name = owner_name
        self.daily_limit = daily_limit
        self.interest_rate = interest_rate
        BankAccount.accounts.append(self)
        self.save_to_file()

    def __str__(self):
        return f"Номер рахунку: {self.account_number}, Баланс: {self.balance}, Власник: {self.owner_name}"

    def deposit(self, amount):
        if amount > 0:
            self.balance.amount += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance.amount and amount <= self.daily_limit:
            self.balance.amount -= amount

    def account_info(self):
        return f"Номер акаунта: {self.account_number}, Баланс: {self.balance}, Власник: {self.owner_name}"

    def transfer(self, recipient, amount):
        if 0 < amount <= self.balance.amount and amount <= self.daily_limit:
            self.balance.amount -= amount
            recipient.deposit(amount)

    def transfer_funds(self, target_account, amount):
        if 0 < amount <= self.balance.amount and amount <= self.daily_limit:
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





