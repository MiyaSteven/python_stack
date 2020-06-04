class BankAccount:
    def __init__(self, interest_rate=0.1, account_balance=0):
        self.account_balance = account_balance
        self.interest_rate = interest_rate
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_account_info(self):
        print(self.account_balance)
        return self
    def yield_interest(self):
        self.account_balance += self.account_balance * self.interest_rate 
        return self

StevensAccount = BankAccount(.2, 1000)
JoesAccount = BankAccount(.15, 2000)

StevensAccount.deposit(500).deposit(500).deposit(750).yield_interest().display_account_info()
JoesAccount.deposit(500).deposit(1000).withdraw(100).withdraw(199).withdraw(201).withdraw(100).yield_interest().display_account_info()

class User:		# declare a class and give it name User
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate=.02, account_balance=0)

    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self

    def make_deposit(self, amount):
        self.account_balance = self.account_balance + amount
        return self

    def display_user_balance(self, account_balance):
        print(self.account_balance)
        return self

    def transfer_funds(self, recipient, amount):
        pass

Steven = User("Steven", "fake@gmail.com")
Joe = User("Joe", "joesEmail@gmail.com")
Peter = User("Peter", "dragon@gmail.com")

Steven.make_deposit(200).make_deposit(300).make_deposit(100).display_user_balance(Steven.account_balance)

Joe.make_deposit(500).make_deposit(1000).make_withdraw(739).make_withdraw(511).display_user_balance(Joe.account_balance)

Peter.make_deposit(10000).make_withdraw(2000).make_withdraw(2000).make_withdraw(2000).display_user_balance(Peter.account_balance)
