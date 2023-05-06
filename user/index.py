class user:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("Name: {}, Account Balance: {} USD".format(self.name, self.account_balance))

    def make_transfer(self, reciver, amount):
        self.account_balance -= amount
        reciver.account_balance += amount


michael = user("Michael")
guido = user("Guido")
monty = user("Monty")

michael.make_deposit(50)
michael.make_deposit(100)
michael.make_deposit(300)
michael.make_withdrawal(200)
michael.display_user_balance()

guido.make_deposit(200)
guido.make_deposit(1000)
guido.make_withdrawal(300)
guido.make_withdrawal(500)
guido.display_user_balance()

monty.make_deposit(1000)
monty.make_withdrawal(100)
monty.make_withdrawal(150)
monty.make_withdrawal(200)
monty.display_user_balance()

michael.display_user_balance()
monty.display_user_balance()
michael.make_transfer(monty, 100)
michael.display_user_balance()
monty.display_user_balance()


