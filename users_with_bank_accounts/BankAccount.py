class BankAccount:
    def __init__(self, balance = 0, rate = 0.01):
        self.balance = balance
        self.rate = rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        self.balance -= amount

    def transfer(self, reciver, amount):
        self.balance -= amount
        reciver.balance += amount

    def yeild_interest(self):
        if self.balance > 0:
            self.balance *= 1+self.rate