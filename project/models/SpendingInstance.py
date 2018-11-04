from abc import ABC
from project import db


class SpendingInstance(db.Model):
    __tablename__ = 'spending_instance'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    account = db.relationship('Account', uselist=False)
    date = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80))
    spending_history_id = db.Column(db.Integer, db.ForeignKey('spending_history.id'))
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __init__(self, amount, account, date, description):
        self.amount = amount
        self.account = account
        self.date = date
        self.description = description

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

    def __str__(self):
        return 'Ate for ' + str(self.amount)

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
        return 'Shopped for ' + str(self.amount)

    __mapper_args__ = {
        'polymorphic_identity': 'retail_spending_instance',
    }
