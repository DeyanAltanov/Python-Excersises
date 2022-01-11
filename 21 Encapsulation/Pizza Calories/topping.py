class Topping:
    def __init__(self, topping_type, weight):
        self.__topping_type = topping_type
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def get_topping_type(self):
        return self.__topping_type

    def set_topping_type(self, new_topping_type):
        self.__topping_type = new_topping_type

    def set_weight(self, new_weight):
        self.__weight = new_weight