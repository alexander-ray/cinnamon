from project import db
from .SpendingHistory import SpendingHistory


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    income = db.Column(db.Integer)
    information = db.relationship('UserInformation', uselist=False)
    accounts = db.relationship('Account')
    spending_history = db.relationship('SpendingHistory', uselist=False, enable_typechecks=True)

    def __init__(self, username, password, info):
        self.id = 22
        self.username = username
        self.password = password
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
