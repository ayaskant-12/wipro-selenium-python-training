# cerate a python program with class name savingsccount and functions deposit in parent class  and  addinterest in the child class

class SavingsAccount:
    def __init__(self, balance = 0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposited amount: ", amount)
        print("Current balance: ", self.balance)

class InterestAccount(SavingsAccount):
    def addInterest(self):
        intrest = self.balance * 0.25
        self.balance += intrest
        print("Intrest added: ", intrest)
        print("Balance after intrest: ", self.balance)

acc = InterestAccount(10000)
acc.deposit(500)
acc.addInterest()

# class multilevel

class SavingsAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

class InterestAccount(SavingsAccount):
    def addInterest(self):
        interest = self.balance * 0.25
        self.balance += interest
        print("Interest added:", interest)

class FinalAccount(InterestAccount):
    def display(self):
        print("Final Balance:", self.balance)

acc = FinalAccount(10000)
acc.deposit(5000)
acc.addInterest()
acc.display()