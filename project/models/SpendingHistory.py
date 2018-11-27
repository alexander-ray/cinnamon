from project import db
from sqlalchemy.ext.hybrid import hybrid_property

class SpendingHistory(db.Model):
    __tablename__ = 'spending_history'
    _id = db.Column(db.Integer, primary_key=True)
    _user_id = db.Column(db.Integer, db.ForeignKey('user._id'))
    _spending_instances = db.relationship('SpendingInstance')

    @hybrid_property
    def spending_instances(self):
        # Sort in reverse chronological order
        """
        Getter for spending instances

        :return: List of spending instances, sorted in reverse chronological order by date
        """
        return list(sorted(self._spending_instances, key=lambda x: x.date, reverse=True))

    def add_spending_instance(self, instance):
        """
        Method to add a spending instance to your spending history

        :param instance: Instance to add
        """
        self._spending_instances.append(instance)
