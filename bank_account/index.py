class bank_account:
    def __init__(self, balance = 0, rate = 0.01):
        self.balance = balance
        self.rate = rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: ${}".format(self.balance))
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance *= 1+self.rate
        return self

mohammed = bank_account(1000, 0.01)
mohammed.deposit(100).display_account_info().withdraw(600).display_account_info().withdraw(600).display_account_info().yeild_interest().display_account_info().deposit(1105).display_account_info().yeild_interest().display_account_info()

first_account = bank_account(1500, 0.02)
second_account = bank_account(1200, 0.01)

first_account.deposit(100).deposit(200).deposit(300).yeild_interest().display_account_info()
second_account.deposit(105).deposit(500).withdraw(500).withdraw(1500).withdraw(200).withdraw(50).yeild_interest().display_account_info()