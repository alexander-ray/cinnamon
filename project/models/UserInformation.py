from project import db

class UserInformation(db.Model):
    __tablename__ = 'user_information'
    id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Integer, nullable=False)
    address = db.relationship('Address', uselist=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, income, address):
        self.income = income
        self.address = address