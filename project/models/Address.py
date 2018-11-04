from project import db
7

class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    zip = db.Column(db.String(80), nullable=False)
    user_info_id = db.Column(db.Integer, db.ForeignKey('user_information.id'))

    def __init__(self, street_address, city, state, zip):
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip = zip
