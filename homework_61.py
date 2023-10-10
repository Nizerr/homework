import unittest
from bank_v2 import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.account1 = BankAccount(12345, 1000, "John", "USD")
        self.account2 = BankAccount(54321, 500, "Alice", "EUR")

    def test_deposit(self):
        self.account1.deposit(200)
        self.assertEqual(self.account1.balance.amount, 1200)

    def test_withdraw(self):
        self.account1.withdraw(600)
        self.assertEqual(self.account1.balance.amount, 400)

    def test_transfer(self):
        self.account1.transfer(self.account2, 300)
        self.assertEqual(self.account1.balance.amount, 700)
        self.assertEqual(self.account2.balance.amount, 800)

    def test_check_account_number(self):
        self.assertTrue(BankAccount.check_account_number(12345))
        self.assertFalse(BankAccount.check_account_number(1234))

    def test_get_average_balance(self):
        self.assertEqual(BankAccount.get_average_balance(), 775.0)

    def test_find_account_by_owner_single_match(self):
        matching_account = BankAccount.find_accounts_by_owner("John")
        self.assertEqual(len(matching_account), 3)
        self.assertEqual(matching_account[0].owner_name, "John")

if __name__ == '__main__':
    unittest.main()
