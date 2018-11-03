from .SpendingHistory import SpendingHistory


class User:
    # TODO
    # Make report generator
    def __init__(self, username, income, info):
        self.id = 22
        self.username = username
        self.income = income
        self.information = info
        self.accounts = []
        self.spending_history = SpendingHistory()

    def get_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None

    def get_account_names(self):
        return [account.name for account in self.accounts]

    # Needed for flask-login
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
