class Account:
    num_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt


print(Account.num_accounts)

account1 = Account('홍길동', 1000)
print(account1.num_accounts)
print(Account.num_accounts)

account2 = Account('임꺽정', 2000)
print(account1.num_accounts)
print(account2.num_accounts)
print(Account.num_accounts)