class user:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("Name: {}, Account Balance: {} USD".format(self.name, self.account_balance))
        return self

    def make_transfer(self, reciver, amount):
        self.account_balance -= amount
        reciver.account_balance += amount
        return self


michael = user("Michael")
guido = user("Guido")
monty = user("Monty")

michael.make_deposit(50).make_deposit(100).make_deposit(300).make_withdrawal(200).display_user_balance()

guido.make_deposit(200).make_deposit(1000).make_withdrawal(300).make_withdrawal(500).display_user_balance()

monty.make_deposit(1000).make_withdrawal(100).make_withdrawal(150).make_withdrawal(200).display_user_balance()

michael.display_user_balance()
monty.display_user_balance()
michael.make_transfer(monty, 100).display_user_balance()
monty.display_user_balance()


