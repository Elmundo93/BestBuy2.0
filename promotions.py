from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass

class PercentageDiscount(Promotion):
    def __init__(self, discount):
        # discount is a percentage (e.g., 20 for 20% off)
        super().__init__(f"{discount}% off")
        self.discount = discount

    def apply_promotion(self, product, quantity) -> float:
        return product.price * quantity * (1 - self.discount / 100)

class SecondItemHalfPrice(Promotion):
    def __init__(self):
        super().__init__("Second item half price")

    def apply_promotion(self, product, quantity) -> float:
        # For every two items, cost = full price + half price.
        pairs = quantity // 2
        remainder = quantity % 2
        return pairs * (product.price + product.price * 0.5) + remainder * product.price

class Buy2Get1Free(Promotion):
    def __init__(self):
        super().__init__("Buy 2, get 1 free")

    def apply_promotion(self, product, quantity) -> float:
        # For every 3 items, the customer pays for 2.
        groups = quantity // 3
        remainder = quantity % 3
        return groups * (2 * product.price) + remainder * product.price