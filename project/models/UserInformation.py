from project import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class UserInformation(Base):
    __tablename__ = 'user_information'
    id = Column(Integer, primary_key=True)
    income = Column(Integer, nullable=False)
    address = relationship('Address', uselist=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, income, address):
        self.income = income
        self.address = address