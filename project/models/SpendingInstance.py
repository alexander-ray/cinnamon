from abc import ABC


class SpendingInstance(ABC):
    def __init__(self, amount, account, date, description):
        self.amount = amount
        self.account = account
        self.date = date
        self.description = description


class DiningSpendingInstance(SpendingInstance):
    def __init__(self, amount, account, date, description):
        super(DiningSpendingInstance, self).__init__(amount,
                                                     account,
                                                     date,
                                                     description)
        self.instance_type = 'Dining'

    def __str__(self):
        return 'Ate for ' + str(self.amount)


class RetailSpendingInstance(SpendingInstance):
    def __init__(self, amount, account, date, description):
        super(RetailSpendingInstance, self).__init__(amount,
                                                     account,
                                                     date,
                                                     description)
        self.instance_type = 'Retail'

    def __str__(self):
        return 'Shopped for ' + str(self.amount)