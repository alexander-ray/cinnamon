from .SpendingInstance import DiningSpendingInstance, RetailSpendingInstance


class SpendingInstanceFactory:
    @staticmethod
    def factory_method(amount, account, date, description, instance_type):
        if instance_type == 'Dining':
            return DiningSpendingInstance(amount, account, date, description)
        return RetailSpendingInstance(amount, account, date, description)