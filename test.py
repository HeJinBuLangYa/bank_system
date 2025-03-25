import unittest
import os
from bank import Bank, Account


class TestBankSystem(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.test_file = "test_bank.csv"

    def test_create_account(self):
        account = self.bank.create_account("Alice", 1000)
        self.assertEqual(account.name, "Alice")
        self.assertEqual(account.balance, 1000)

    def test_deposit(self):
        account = self.bank.create_account("Bob")
        account.deposit(500)
        self.assertEqual(account.balance, 500)

    def test_withdraw(self):
        account = self.bank.create_account("Charlie", 800)
        account.withdraw(300)
        self.assertEqual(account.balance, 500)
        with self.assertRaises(ValueError):
            account.withdraw(600)

    def test_transfer(self):
        acc1 = self.bank.create_account("David", 1000)
        acc2 = self.bank.create_account("Eve", 500)
        self.bank.transfer(acc1.account_id, acc2.account_id, 300)
        self.assertEqual(acc1.balance, 700)
        self.assertEqual(acc2.balance, 800)

    def test_csv_operations(self):
        # Create test data
        acc1 = self.bank.create_account("Frank", 1500)
        acc2 = self.bank.create_account("Grace", 2000)

        # Save and load
        self.bank.save_to_csv(self.test_file)
        new_bank = Bank()
        new_bank.load_from_csv(self.test_file)

        # Verify data
        self.assertEqual(len(new_bank.accounts), 2)
        loaded_acc = new_bank.find_account(acc1.account_id)
        self.assertIsNotNone(loaded_acc)
        self.assertEqual(loaded_acc.balance, 1500)

        # Clean up test files
        os.remove(self.test_file)


if __name__ == '__main__':
    unittest.main()