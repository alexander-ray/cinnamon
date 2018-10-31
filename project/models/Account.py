from project import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    sum_withdrawls = Column(Integer, nullable=False, default=0)
    user_id = Column(Integer, ForeignKey('user.id'))
    def __init__(self, name):
        self.name = name
        self.sum_withdrawls = 0

    def withdraw(self, amount):
        self.sum_withdrawls += amount
