from project import Base
from .SpendingHistory import SpendingHistory
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), unique=True, nullable=False)
    income = Column(Integer, nullable=False)
    information = relationship('UserInformation', uselist=False)
    accounts = relationship('Account')
    spending_history = relationship('SpendingHistory', uselist=False)

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
