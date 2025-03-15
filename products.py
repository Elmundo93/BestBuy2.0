class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def reduce_quantity(self, amount):
        if amount > self.quantity:
            raise ValueError("Not enough stock available.")
        self.quantity -= amount
        return True

    def is_active(self):
        return self.quantity > 0