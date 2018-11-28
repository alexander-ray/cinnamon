from project import db
import math
from abc import abstractmethod, ABCMeta
from sqlalchemy.ext.hybrid import hybrid_property
from project import mail
from flask_mail import Message
from flask_login import current_user
# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_decorator.htm
# https://stackoverflow.com/questions/22976445/
# https://stackoverflow.com/questions/9606551/
# https://stackoverflow.com/questions/32341408/
# https://docs.sqlalchemy.org/en/latest/orm/inheritance.html#abstract-concrete-classes
# https://docs.sqlalchemy.org/en/latest/orm/self_referential.html


class BaseAccount(db.Model):
    __metaclass__ = ABCMeta

    __tablename__ = 'base_account'

    _id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(80), nullable=False)
    _expenditure = db.Column(db.Integer, default=0)
    _user_id = db.Column(db.Integer, db.ForeignKey('user._id'))
    # Id pretty much needs to be in base
    _decorator_id = db.Column(db.Integer, db.ForeignKey('base_account._id'))
    _type = db.Column(db.String(80))

    @abstractmethod
    def withdraw(self, amount):
        """
        Abstract withdraw method, to be implemented by subclasses

        :param amount: Amount to withdraw
        """
        pass

    @abstractmethod
    def __str__(self):
        """
        Abstract string method to ensure subclasses write implementations
        """
        pass

    @hybrid_property
    def name(self):
        """
        Getter for account name

        :return: Name of account
        """
        return self._name

    @hybrid_property
    def expenditure(self):
        """
        Getter for total expenditure

        :return: Sum of all spending in this account
        """
        return self._expenditure

    __mapper_args__ = {
        'polymorphic_identity': 'base_account',
        'polymorphic_on': _type
    }


class ConcreteAccount(BaseAccount):
    def __init__(self, name):
        BaseAccount.__init__(self)
        self._name = name
        self._decorator_id = None
        self._expenditure = 0

    def withdraw(self, amount):
        """
        Method for withdrawing money from an account

        :param amount: Amount of money to withdraw
        :return: Current total expenditure. Needed for decorator design pattern due to SQLAlchemy constraints
        """
        self._expenditure += amount
        return self._expenditure

    def __str__(self):
        return 'WITHDRAWLS: ' + '{0:.2f}'.format(self._expenditure) + '    '

    __mapper_args__ = {
        'polymorphic_identity': 'concrete_account',
    }


class BaseAccountDecorator(BaseAccount):
    __metaclass__ = ABCMeta
    _decorator = db.relationship('BaseAccount', uselist=False,
                                 backref=db.backref('_dec', remote_side=[BaseAccount._id]))

    def __init__(self, dec):
        self._decorator = dec
        self._name = self._decorator.name

    @abstractmethod
    def __str__(self):
        pass

    __mapper_args__ = {
        'polymorphic_identity': 'base_account_decorator',
    }


class AccountEmailDecorator(BaseAccountDecorator):
    def __init__(self, dec):
        BaseAccountDecorator.__init__(self, dec)

    def withdraw(self, amount):
        """
        Withdraw method for email decorator class. Calls other withdraw methods, then sends email with details

        :param amount: Amount of money to withdraw
        :return: Current total expenditure. Needed for decorator design pattern due to SQLAlchemy constraints
        """
        self._expenditure = self._decorator.withdraw(amount)
        self._send_mail(amount)
        return self._expenditure

    def __str__(self):
        return self._decorator.__str__()

    def _send_mail(self, amount):
        """
        Sends mail to current user

        :param amount: Amount of withdrawal that prompted an email
        """
        message = Message(
            'Cinnamon Account Update',
            sender='1alexray@gmail.com',
            recipients=[current_user.email])
        message.html = '<p>Recent Withdrawl: ' + \
                       '{0:.2f}'.format(amount) + \
                       '</p>' + current_user.summary_generator.summary_template_method()
        mail.send(message)

    __mapper_args__ = {
        'polymorphic_identity': 'account_withdrawl_decorator',
    }


class AccountSavingsDecorator(BaseAccountDecorator):
    _sum_savings = db.Column(db.Integer, default=0)

    def __init__(self, dec):
        BaseAccountDecorator.__init__(self, dec)
        self._sum_savings = 0

    def withdraw(self, amount):
        """
        Withdraw method for savings decorator. Calls other withdraw methods, adds to savings (rounded up to nearest
        dollar), and returns current sum of withdrawals.

        :param amount: Amount of money to withdraw
        :return: Current total expenditure. Needed for decorator design pattern due to SQLAlchemy constraints
        """
        self._expenditure = self._decorator.withdraw(amount)
        self._sum_savings += math.ceil(amount) - amount
        return self._expenditure

    def __str__(self):
        # https://stackoverflow.com/questions/1995615/
        ret = 'SAVINGS: ' + '{0:.2f}'.format(self._sum_savings) + '    '
        return self._decorator.__str__() + ret

    __mapper_args__ = {
        'polymorphic_identity': 'account_savings_decorator',
    }
