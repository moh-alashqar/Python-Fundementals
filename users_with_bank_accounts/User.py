from BankAccount import BankAccount
class User:
    def __init__(self, full_name):
        self.name = full_name
        self.accounts = {}

    def create_account(self, account_type, initial_amount, interest_rate):
        self.accounts[account_type] = BankAccount(initial_amount, interest_rate)
        return self

    def make_deposit(self, amount, account_type):
        self.accounts[account_type].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_type):
        self.accounts[account_type].withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"Name: {self.name}")
        for account_type, account in self.accounts.items():
            print(f"{account_type} balance: {account.balance}")
        return self

    def make_transfer(self, reciver, amount, sender_account_type, reciver_account_type):
        self.accounts[sender_account_type].transfer(reciver.accounts[reciver_account_type], amount)
        return self    

mohammed = User("Mohammed Alashqar")
ahmed = User('Ahmad')

ahmed.create_account('saving_account_usd', 0, 0)

mohammed.create_account('saving_account_usd', 1000, 0.01).display_user_balance().create_account('current_account_ils', 2000, 0.02).display_user_balance().make_deposit(500, 'saving_account_usd').display_user_balance().make_deposit(1000, 'current_account_ils').display_user_balance().make_withdrawal(200, 'saving_account_usd').display_user_balance().make_withdrawal(300, 'current_account_ils').display_user_balance().make_transfer(ahmed, 500, 'saving_account_usd', 'saving_account_usd').display_user_balance()

ahmed.display_user_balance()
