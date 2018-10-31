class Account:
    def __init__(self, name):
        self.name = name
        self.sum_withdrawls = 0

    def withdraw(self, amount):
        self.sum_withdrawls += amount
