from project import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class SpendingHistory(Base):
    __tablename__ = 'spending_history'
    id = Column(Integer, primary_key=True)
    spending_instances = relationship('SpendingInstance')
    user_id = Column(Integer, ForeignKey('user.id'))
    def get_spending_instances(self):
        return self.spending_instances

    def add_spending_instance(self, instance):
        self.spending_instances.append(instance)
