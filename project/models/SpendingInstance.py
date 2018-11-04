from project import db
from project.models.SpendingType import SpendingType
import datetime
import pytz

class SpendingInstance(db.Model):
    # Only superclass gets tablename
    __tablename__ = 'spending_instance'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    account = db.relationship('Account', uselist=False)
    date = db.Column(db.Date, default=datetime.datetime.now())
    description = db.Column(db.String(80))
    # Field for distinguishing between subclasses
    type = db.Column(db.String(80))
    spending_history_id = db.Column(db.Integer, db.ForeignKey('spending_history.id'))
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __init__(self, amount, account, date, description):
        self.amount = amount
        self.account = account
        self.date = date
        self.description = description

    # Setup for single table polymorphic stuff in sqlalchemy
    # https://docs.sqlalchemy.org/en/latest/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'spending_instance',
        'polymorphic_on': type
    }


class DiningSpendingInstance(SpendingInstance):
    def __init__(self, amount, account, date, description):
        super(DiningSpendingInstance, self).__init__(amount,
                                                     account,
                                                     date,
                                                     description)
        self.amount += self.amount * 0.2

    def __str__(self):
        return SpendingType.DINING.value

    __mapper_args__ = {
        'polymorphic_identity': 'dining_spending_instance',
    }


class RetailSpendingInstance(SpendingInstance):
    def __init__(self, amount, account, date, description):
        super(RetailSpendingInstance, self).__init__(amount,
                                                     account,
                                                     date,
                                                     description)

    def __str__(self):
        return SpendingType.RETAIL.value

    __mapper_args__ = {
        'polymorphic_identity': 'retail_spending_instance',
    }
