from project import db

# TODO:
# Implement decorator to dynamically add functionality to accounts
class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    sum_withdrawls = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name):
        self.name = name
        self.sum_withdrawls = 0

    def withdraw(self, amount):
        self.sum_withdrawls += amount
