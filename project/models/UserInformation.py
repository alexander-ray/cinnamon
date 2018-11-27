from project import db
from sqlalchemy.ext.hybrid import hybrid_property


class UserInformation(db.Model):
    __tablename__ = 'user_information'
    _id = db.Column(db.Integer, primary_key=True)
    _income = db.Column(db.Integer, nullable=False)
    _address = db.relationship('Address', uselist=False)
    _user_id = db.Column(db.Integer, db.ForeignKey('user._id'))

    def __init__(self, income, address):
        self.income = income
        self.address = address

    @hybrid_property
    def income(self):
        """
        Getter for user income

        :return: User income
        """
        return self._income

    @income.setter
    def income(self, income):
        """
        Setter for user income

        :param income: New income
        """
        self._income = income

    @hybrid_property
    def address(self):
        """
        Getter for user address

        :return: User address object
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Setter for user address

        :param address: User address object
        """
        self._address = address
