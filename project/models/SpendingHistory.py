class SpendingHistory:
    def __init__(self):
        self.spending_instances = []

    def get_spending_instances(self):
        return self.spending_instances

    def add_spending_instance(self, instance):
        self.spending_instances.append(instance)
