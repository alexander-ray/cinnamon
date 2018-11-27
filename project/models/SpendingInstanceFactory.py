from .SpendingInstance import DiningSpendingInstance, RetailSpendingInstance
from .SpendingType import SpendingType


class SpendingInstanceFactory:
    @staticmethod
    def factory_method(amount, account, date, description, instance_type):
        """
        Static factory method for simple factory design pattern, to create spending instances. Types defined in
        SpendingType

        :param amount: Amount of instance
        :param account: Account object
        :param date: Date object
        :param description: Optional description
        :param instance_type: Type from SpendingType
        :return: Spending instance object
        """
        if instance_type == SpendingType.DINING.value:
            return DiningSpendingInstance(amount, account, date, description)
        return RetailSpendingInstance(amount, account, date, description)
