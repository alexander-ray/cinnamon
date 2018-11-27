from project import db
from sqlalchemy.ext.hybrid import hybrid_property


class Address(db.Model):
    __tablename__ = 'address'
    _id = db.Column(db.Integer, primary_key=True)
    _street_address = db.Column(db.String(80), nullable=False)
    _city = db.Column(db.String(80), nullable=False)
    _state = db.Column(db.String(80), nullable=False)
    _zip = db.Column(db.String(80), nullable=False)
    _user_info_id = db.Column(db.Integer, db.ForeignKey('user_information._id'))

    def __init__(self, street_address, city, state, zip):
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip = zip

    @hybrid_property
    def street_address(self):
        """
        Getter for street address

        :return: Street address
        """
        return self._street_address

    @hybrid_property
    def city(self):
        """
        Getter for city

        :return: City
        """
        return self._city

    @hybrid_property
    def state(self):
        """
        Getter for state

        :return: State
        """
        return self._state

    @hybrid_property
    def zip(self):
        """
        Getter for zip code

        :return: Zip code
        """
        return self._zip
