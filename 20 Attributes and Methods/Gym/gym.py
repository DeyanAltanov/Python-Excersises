class Gym:
    customers = []
    trainers = []
    equipment = []
    plans = []
    subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.customers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.customers.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.customers.append(plan)

    def add_subscription(self, subscription):
        present = False
        for s in self.subscriptions:
            if s.id == subscription.id:
                present = True
                break
        if not present:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        result = ""
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                result += f"Subscription <{subscription.id}> on {subscription.date}"
                result += '\n'
                break
        for customer in self.customers:
            if customer.id == subscription_id:
                result += f"Customer <{customer.id}> {customer.name}; Address: {customer.address}; Email: {customer.email}\n"
                break
        for trainer in self.trainers:
            if trainer.id == subscription_id:
                result += f"Trainer <{trainer.id}> {trainer.name}\n"
                break
        for equipment in self.equipment:
            if equipment.id == subscription_id:
                result += f"Equipment <{equipment.id}> {equipment.name}\n"
                break
        for plan in self.plans:
            if plan.id == subscription_id:
                result += f"Plan <{plan.id}> with duration {plan.duration} minutes"
                break
        return result