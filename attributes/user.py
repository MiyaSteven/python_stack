class BankAccount:
    def __init__(self, interest_rate=0.1, balance=0, account_type="checking"):
        self.balance = balance
        self.interest_rate = interest_rate
        self.account_type = {}
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        self.balance += self.balance * self.interest_rate 
        return self

StevensAccount = BankAccount(.2, 1000)
JoesAccount = BankAccount(.15, 2000)
StevensAccount.account_type

StevensAccount.deposit(500).deposit(500).deposit(750).yield_interest().display_account_info()
JoesAccount.deposit(500).deposit(1000).withdraw(100).withdraw(199).withdraw(201).withdraw(100).yield_interest().display_account_info()

class User:		# declare a class and give it name User
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate=.02, balance=0, account_type="checking")

    def make_withdraw(self, amount):
        self.account.balance -= amount
        return self

    def make_deposit(self, amount):
        self.account.balance = self.account.balance + amount
        return self

    def display_user_balance(self):
        print(self.account.balance)
        return self

    def transfer_funds(self, recipient, amount):
        pass

Steven = User("Steven", "fake@gmail.com")
Joe = User("Joe", "joesEmail@gmail.com")
Peter = User("Peter", "dragon@gmail.com")

Steven.account.deposit(200).deposit(300).deposit(100).display_user_balance(Steven.account.balance)

Joe.make_deposit(500).make_deposit(1000).make_withdraw(739).make_withdraw(511).display_user_balance(Joe.account.balance)

Peter.make_deposit(10000).make_withdraw(2000).make_withdraw(2000).make_withdraw(2000).display_user_balance(Peter.account.balance)
