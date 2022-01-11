class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
        self.items_count = 0

    @staticmethod
    def can_add_item(count, capacity):
        return count < capacity

    @staticmethod
    def can_remove_item(items, item_name, amount):
        return item_name in items and amount <= items[item_name]

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, size // 2)

    def add_item(self, item):
        if not self.can_add_item(self.items_count, self.capacity):
            return "Not enough capacity in the store"
        self.items_count += 1
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1
        return f"{item} added to the store"

    def remove_item(self, item, amount):
        if not self.can_remove_item(self.items, item, amount):
            return f"Cannot remove {amount} {item}"
        self.items_count -= amount
        self.items[item] -= amount
        return f"{amount} {item} removed from the store"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"