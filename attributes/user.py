class User:		# declare a class and give it name User
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_withdraw(self, amount):
        self.account_balance -= amount
    def make_deposit(self, amount):
        self.account_balance = self.account_balance + amount
    def display_user_balance(self, account_balance):
        print(self.account_balance)
    def transfer_funds(self, recipient, amount):
        pass

Steven = User("Steven", "fake@gmail.com")
Joe = User("Joe", "joesEmail@gmail.com")
Peter = User("Peter", "dragon@gmail.com")

Steven.make_deposit(200)
Steven.make_deposit(300)
Steven.make_deposit(100)
Steven.display_user_balance(Steven.account_balance)

Joe.make_deposit(500)
Joe.make_deposit(1000)
Joe.make_withdraw(739)
Joe.make_withdraw(511)
Joe.display_user_balance(Joe.account_balance)

Peter.make_deposit(10000)
Peter.make_withdraw(2000)
Peter.make_withdraw(2000)
Peter.make_withdraw(2000)
Peter.display_user_balance(Peter.account_balance)