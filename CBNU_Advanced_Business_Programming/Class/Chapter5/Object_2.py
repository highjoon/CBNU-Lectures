class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        print("통장에 ", amount, "가 출금되었음.")
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print("통장에서 ", amount, "가 입금되었음")
        return self.balance

    def status(self):
        print("현재 잔액 = ", self.balance)

a = BankAccount()
a.deposit(100)
a.withdraw(10)
a.withdraw(40)
a.status()



