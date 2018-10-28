class User:
    def __init__(self, username, income, info):
        self.username = username
        self.income = income
        self.information = info
        self.accounts = {}
        self.spending_history = None

