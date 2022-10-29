class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.subscriptions = []
        self.plans = []

    @staticmethod
    def add(some_list, some_object):
        if Gym.check_object(some_object, some_list):
            some_list.append(some_object)

    @staticmethod
    def check_object(some_object, some_list):
        if some_object not in some_list:
            return True
        return False

    @staticmethod
    def find_by_id(some_list, id):
        for value in some_list:
            if value.id == id:
                return value

    def add_customer(self, customer):
        Gym.add(self.customers, customer)

    def add_trainer(self, trainer):
        Gym.add(self.trainers, trainer)

    def add_equipment(self, equipment):
        Gym.add(self.equipment, equipment)

    def add_plan(self, plan):
        Gym.add(self.plans, plan)

    def add_subscription(self, subscription):
        Gym.add(self.subscriptions, subscription)

    def subscription_info(self, subscription_id):
        subscription = self.find_by_id(self.subscriptions, subscription_id)
        customer = self.find_by_id(self.customers, subscription_id)
        trainer = self.find_by_id(self.trainers, subscription_id)
        plan = self.find_by_id(self.plans, subscription_id)
        equipment = self.find_by_id(self.equipment, subscription_id)
        ll = [subscription, customer, trainer, equipment, plan]
        return '\n'.join(str(x) for x in ll)