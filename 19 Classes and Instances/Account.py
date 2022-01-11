class Account:
    def __init__(self, id, name, balance=0):
        self.id = int(id)
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += int(amount)
        return self.balance

    def debit(self, amount):
        if int(amount) <= self.balance:
            self.balance -= int(amount)
            return self.balance
        return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"
