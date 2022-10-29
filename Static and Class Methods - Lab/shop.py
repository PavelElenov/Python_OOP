class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type, capacity=10):
        return cls(name, type, capacity)

    def add_item(self, item_name):
        if sum(self.items.values()) == self.capacity:
            return "Not enough capacity in the shop"
        if item_name in self.items:
            self.items[item_name] += 1
        else:
            self.items[item_name] = 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items and amount <= self.items[item_name]:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
