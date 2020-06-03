# attributes are characteristics of an object defined in a "magic method" called __init__, which method is called when a new object is instantiated
class User:		# declare a class and give it name User
    def __init__(self):
        self.name = "Steven"
        self.email = "swm9220@gmail.com"
        self.account_balance = 0

# instantiate a couple of new Users
guido = User()
monty = User()

# access instance's attributes
print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

# set the values of User object instance's
guido.name = "Guido"
monty.name = "Monty"

class User:
    def __init__(self, username, email_address): # now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

guido.make_deposit(100)

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50
