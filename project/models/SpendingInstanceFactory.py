from .SpendingInstance import DiningSpendingInstance, RetailSpendingInstance
from .SpendingType import SpendingType


class SpendingInstanceFactory:
    @staticmethod
    def factory_method(amount, account, date, description, instance_type):
        if instance_type == SpendingType.DINING:
            return DiningSpendingInstance(amount, account, date, description)
        return RetailSpendingInstance(amount, account, date, description)
