from bank import Bank

# 初始化银行系统
bank = Bank()

# 创建账户
alice = bank.create_account("Alice", 1000)
bob = bank.create_account("Bob", 500)

# 存款
alice.deposit(200)

# 转账
bank.transfer(alice.account_id, bob.account_id, 300)

# 保存状态
bank.save_to_csv("bank_data.csv")

# 加载状态
new_bank = Bank()
new_bank.load_from_csv("bank_data.csv")