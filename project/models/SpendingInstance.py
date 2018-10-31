from abc import ABC
from project import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class SpendingInstance(Base):
    __tablename__ = 'spending_instance'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    account = relationship('Account', uselist=False)
    date = Column(String(80), nullable=False)
    description = Column(String(80), nullable=False)
    spending_history_id = Column(Integer, ForeignKey('spending_history.id'))
    account_id = Column(Integer, ForeignKey('account.id'))
    def __init__(self, amount, account, date, description):
        self.amount = amount
        self.account = account
        self.date = date
        self.description = description


class DiningSpendingInstance(SpendingInstance):
    restaurant = Column(String(80), nullable=False)

    def __init__(self, amount, account, date, description):
        super(DiningSpendingInstance, self).__init__(amount,
                                                     account,
                                                     date,
                                                     description)
        self.restaurant = 'Dining'

    def __str__(self):
        return 'Ate for ' + str(self.amount)


class RetailSpendingInstance(SpendingInstance):
    store = Column(String(80), nullable=False)

    def __init__(self, amount, account, date, description):
        super(RetailSpendingInstance, self).__init__(amount,
                                                     account,
                                                     date,
                                                     description)
        self.store = 'Retail'

    def __str__(self):
        return 'Shopped for ' + str(self.amount)