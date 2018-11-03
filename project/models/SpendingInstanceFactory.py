from .SpendingInstance import DiningSpendingInstance, RetailSpendingInstance


class SpendingInstanceFactory:
    # TODO
    # Use enum instead of simple strings
    @staticmethod
    def factory_method(amount, account, date, description, instance_type):
        if instance_type == 'Dining':
            return DiningSpendingInstance(amount, account, date, description)
        return RetailSpendingInstance(amount, account, date, description)
