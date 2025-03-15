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


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        return f"{self.name} (Non-stocked), Price: ${self.price}"

    def reduce_quantity(self, amount):

        return True


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        """
        :param maximum: Maximum quantity allowed per order.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        return (f"{self.name} (Limited to {self.maximum} per order), "
                f"Price: ${self.price}, Quantity: {self.quantity}")

    def reduce_quantity(self, amount):
        if amount > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} units of {self.name} per order.")
        return super().reduce_quantity(amount)