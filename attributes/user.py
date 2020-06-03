class User:		# declare a class and give it name User
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
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