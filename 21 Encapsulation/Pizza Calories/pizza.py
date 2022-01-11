class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}
        self.toppings = {}

    def get_name(self):
        return self.__name

    def get_dough(self):
        return self.__dough

    def get_toppings_capacity(self):
        return self.__toppings_capacity

    def set_name(self, new_name):
        self.__name = new_name

    def set_dough(self, new_dough):
        self.__dough = new_dough

    def set_toppings_capacity(self, new_capacity):
        self.__toppings_capacity = new_capacity

    def add_topping(self, topping):
        if topping.get_topping_type() in self.toppings:
            self.toppings[topping.get_topping_type()] += topping.get_weight()
        elif len(self.toppings) == self.__toppings_capacity:
            raise ValueError("Not enough space for another topping")
        else:
            self.toppings[topping.get_topping_type()] = topping.get_weight()

    def calculate_total_weight(self):
        total_weight = self.__dough.get_weight()
        for topping in self.toppings:
            total_weight += self.toppings[topping]
        return total_weight