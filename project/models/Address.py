from project import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_address = Column(String(80), nullable=False)
    city = Column(String(80), nullable=False)
    state = Column(String(80), nullable=False)
    zip = Column(String(80), nullable=False)
    user_info_id = Column(Integer, ForeignKey('user_information.id'))
    def __init__(self, street_address, city, state, zip):
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip = zip
