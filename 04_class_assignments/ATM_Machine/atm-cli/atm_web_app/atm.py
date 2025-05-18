class ATM:
    def __init__(self) -> None:
        self.pin = "1234"
        self.balance = 1000.0
        self.is_authenticated = False

    def check_pin(self, input_pin):
        if input_pin == self.pin:
            self.is_authenticated = True
        else:
            self.is_authenticated = False

    def deposit(self, amount):
        if self.is_authenticated and amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if self.is_authenticated and amount > 0 and amount <= self.balance:
            self.balance -= amount
