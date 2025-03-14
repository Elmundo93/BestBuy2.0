class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def reduce_quantity(self, amount):
        if amount > self.quantity:
            print("Not enough stock available.")
            return False
        self.quantity -= amount
        return True