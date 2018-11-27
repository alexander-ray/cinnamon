from project import db
from .SpendingHistory import SpendingHistory
from .ReportGenerator import CSVReportGenerator
from .SummaryGenerator import TotalExpenditureSummaryGenerator
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    __tablename__ = 'user'

    _id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    _email = db.Column(db.String(80), unique=True, nullable=False)
    _password = db.Column(db.String(80), nullable=False)
    _information = db.relationship('UserInformation', uselist=False)
    _accounts = db.relationship('BaseAccount')
    _spending_history = db.relationship('SpendingHistory', uselist=False, enable_typechecks=True)
    _report_generator = db.relationship('ReportGenerator', uselist=False, enable_typechecks=True)
    _summary_generator = db.relationship('SummaryGenerator', uselist=False, enable_typechecks=True)

    def __init__(self, email, password, info):
        self._email = email
        self._password = password
        self._information = info
        self._accounts = []
        self._spending_history = SpendingHistory()
        # Default to CSV, don't ask user when they first sign up
        self._report_generator = CSVReportGenerator(filename='export')
        # Default to total expenditure, don't ask user when they first sign up
        self._summary_generator = TotalExpenditureSummaryGenerator()

    @hybrid_property
    def email(self):
        """
        Getter for user email

        :return: User email
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Setter for user email

        :param email: New email address
        """
        self._email = email

    @hybrid_property
    def password(self):
        """
        Getter for user password

        :return: User password
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Setter for user password

        :param password: New password
        """
        self._password = password

    @hybrid_property
    def information(self):
        """
        Getter for user information object

        :return: User information object
        """
        return self._information

    @information.setter
    def information(self, information):
        """
        Setter for user information object

        :param information: Information object
        """
        self._information = information

    @hybrid_property
    def accounts(self):
        """
        Getter for list of user accounts

        :return: List of user accounts
        """
        return self._accounts

    @hybrid_property
    def spending_history(self):
        """
        Getter for user spending history

        :return: Spending history object
        """
        return self._spending_history

    @hybrid_property
    def report_generator(self):
        """
        Getter for report generator object

        :return: Report generator object
        """
        return self._report_generator

    @report_generator.setter
    def report_generator(self, report_generator):
        """
        Setter for report generator object. Needed for strategy design pattern.

        :param report_generator: Report generator object
        """
        self._report_generator = report_generator

    @hybrid_property
    def summary_generator(self):
        """
        Getter for summary generator object

        :return: Summary generator object
        """
        return self._summary_generator

    @summary_generator.setter
    def summary_generator(self, summary_generator):
        """
        Setter for summary generator object. Needed for strategy design pattern.

        :param summary_generator: Summary generator object
        """
        self._summary_generator = summary_generator

    def get_account(self, name):
        """
        Get user account by name

        :param name: Name of user account
        :return: Account object or null if not found
        """
        for account in self._accounts:
            if account.name == name:
                return account
        return None

    @property
    def account_names(self):
        """
        Account names property to retrieve list of account names

        :return: List of account names associated with user
        """
        return [account.name for account in self._accounts]

    # Needed for flask-login
    def is_authenticated(self):
        """
        flask-login method

        :return: True
        """
        return True

    def is_active(self):
        """
        flask-login method

        :return: True
        """
        return True

    def is_anonymous(self):
        """
        flask-login method

        :return: False
        """
        return False

    def get_id(self):
        """
        flask-login method for id retrieval

        :return: User id
        """
        return self._id
