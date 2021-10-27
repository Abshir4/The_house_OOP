class Account:
    # Construct an Account object
    def __init__(self, pin, balance=0, cash=0):
        self.pin = pin
        self.balance = balance
        self.cash = cash

    def getPin(self):
        return self.pin

    def getBalance(self):
        return self.balance

    def getCash(self):
        return self.cash

    def withdraw(self, amount):
        self.balance -= amount
        self.cash += amount

    def deposit(self, amount):
        self.balance += amount

    def pay_card(self, amount):
        self.balance -= amount

    def pay_cash(self, amount):
        self.cash -= amount