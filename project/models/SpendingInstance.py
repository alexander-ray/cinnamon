from project import db
from project.models.SpendingType import SpendingType
import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from abc import abstractmethod, ABCMeta


class SpendingInstance(db.Model):
    # Only superclass gets tablename
    __tablename__ = 'spending_instance'
    # Make abstract
    __metaclass__ = ABCMeta

    _id = db.Column(db.Integer, primary_key=True)
    _amount = db.Column(db.Integer, nullable=False)
    _account = db.relationship('BaseAccount', uselist=False)
    _date = db.Column(db.Date, default=datetime.datetime.now())
    _description = db.Column(db.String(80))
    # Field for distinguishing between subclasses
    _type = db.Column(db.String(80))
    _spending_history_id = db.Column(db.Integer, db.ForeignKey('spending_history._id'))
    _account_id = db.Column(db.Integer, db.ForeignKey('base_account._id'))

    def __init__(self, amount, account, date, description):
        self._amount = amount
        self._account = account
        self._date = date
        self._description = description

    @hybrid_property
    def id(self):
        """
        Getter for id

        :return: Id
        """
        return self._id

    @hybrid_property
    def amount(self):
        """
        Getter for spending instance amount

        :return: Amount
        """
        return self._amount

    @hybrid_property
    def date(self):
        """
        Getter for spending instance date

        :return: Date
        """
        return self._date

    @hybrid_property
    def account(self):
        """
        Getter for account associated with spending instance

        :return: Account
        """
        return self._account

    @hybrid_property
    def description(self):
        """
        Getter for description associated with spending instance

        :return: Description
        """
        return self._description

    @abstractmethod
    def __str__(self):
        """
        Abstract string method to ensure subclasses write implementations
        """
        pass

    # Setup for single table polymorphic stuff in sqlalchemy
    # https://docs.sqlalchemy.org/en/latest/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'spending_instance',
        'polymorphic_on': _type
    }


class DiningSpendingInstance(SpendingInstance):
    def __init__(self, amount, account, date, description):
        super(DiningSpendingInstance, self).__init__(amount,
                                                     account,
                                                     date,
                                                     description)
        self._amount += self._amount * 0.15

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
