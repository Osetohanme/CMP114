class Account:
    def __init__(self):
        self.name = "Isaac"
        self.account_number = 4247106018
        self.account_balance = 200000

    def deposite(self, amount):
        self.account_balance = self.account_balance + amount
        print(self.account_balance)

    def withdraw(self, amount):
        self.account_balance = self.account_balance - amount
        print(self.account_balance)