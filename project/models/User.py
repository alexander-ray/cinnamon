from .SpendingHistory import SpendingHistory


class User:
    def __init__(self, username, income, info):
        self.id = 22
        self.username = username
        self.income = income
        self.information = info
        self.accounts = {}
        self.spending_history = SpendingHistory()

    # https://github.com/realpython/flask-registration/blob/master/project/models.py
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
