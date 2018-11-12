from project import db


class SpendingHistory(db.Model):
    __tablename__ = 'spending_history'
    id = db.Column(db.Integer, primary_key=True)
    spending_instances = db.relationship('SpendingInstance')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def get_spending_instances(self):
        # Sort in reverse chronological order
        return list(sorted(self.spending_instances, key=lambda x: x.date, reverse=True))

    def add_spending_instance(self, instance):
        self.spending_instances.append(instance)
