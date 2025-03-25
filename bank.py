import csv
from typing import List, Optional


class Account:
    """Bank account class  银行账户类"""

    def __init__(self, account_id: str, name: str, balance: float = 0.0):
        self.account_id = account_id
        self.name = name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Deposit money 存款"""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraw money 取款"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount


class Bank:
    """Core banking system class 银行系统核心类"""

    def __init__(self):
        self.accounts: List[Account] = []

    def create_account(self, name: str, initial_balance: float = 0.0) -> Account:
        """Create a new account 创建新账户"""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")  #初始余额不能为负数
        account_id = f"ACC{len(self.accounts) + 1:04d}"
        account = Account(account_id, name, initial_balance)
        self.accounts.append(account)
        return account

    def find_account(self, account_id: str) -> Optional[Account]:
        """Find account by ID 根据ID查找账户"""
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None

    def transfer(self, from_id: str, to_id: str, amount: float) -> None:
        """Transfer funds between accounts 转账操作"""
        from_account = self.find_account(from_id)
        to_account = self.find_account(to_id)

        if not from_account or not to_account:
            raise ValueError("Account does not exist") #账户不存在

        if from_account.balance < amount:
            raise ValueError("Transfer amount exceeds balance") #转账金额超过余额

        from_account.withdraw(amount)
        to_account.deposit(amount)

    def save_to_csv(self, filename: str) -> None:
        """Save data to CSV file 保存数据到CSV文件"""
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["account_id", "name", "balance"])
            for account in self.accounts:
                writer.writerow([
                    account.account_id,
                    account.name,
                    account.balance
                ])

    def load_from_csv(self, filename: str) -> None:
        """Load data from CSV file 从CSV文件加载数据"""
        self.accounts.clear()
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.accounts.append(Account(
                    row['account_id'],
                    row['name'],
                    float(row['balance'])
                ))