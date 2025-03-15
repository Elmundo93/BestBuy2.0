

class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None  # New instance variable to hold a Promotion

    def __str__(self):
        base = f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"
        if self.promotion is not None:
            base += f", Promotion: {self.promotion.name}"
        return base

    def reduce_quantity(self, amount):
        if amount > self.quantity:
            raise ValueError("Not enough stock available.")
        self.quantity -= amount
        return True

    def is_active(self):
        return self.quantity > 0


    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion


    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity")
        if not isinstance(self, NonStockedProduct) and quantity > self.quantity:
            raise ValueError("Not enough stock available.")
        if self.promotion:
            total_cost = self.promotion.apply_promotion(self, quantity)
        else:
            total_cost = self.price * quantity
        if not isinstance(self, NonStockedProduct):
            self.reduce_quantity(quantity)
        return total_cost

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        base = f"{self.name} (Non-stocked), Price: ${self.price}"
        if self.promotion is not None:
            base += f", Promotion: {self.promotion.name}"
        return base

    def reduce_quantity(self, amount):
        # Non-stocked products do not reduce quantity.
        return True

    def __str__(self):
        return self.show()

class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        """
        :param maximum: Maximum quantity allowed per order.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        base = (f"{self.name} (Limited to {self.maximum} per order), "
                f"Price: ${self.price}, Quantity: {self.quantity}")
        if self.promotion is not None:
            base += f", Promotion: {self.promotion.name}"
        return base

    def reduce_quantity(self, amount):
        if amount > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} units of {self.name} per order.")
        return super().reduce_quantity(amount)

    def __str__(self):
        return self.show()