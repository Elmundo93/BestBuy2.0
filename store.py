from products import Product
from products import NonStockedProduct
from products import LimitedProduct
from promotions import PercentageDiscount,Buy2Get1Free,SecondItemHalfPrice

class Store:
    def __init__(self):
        self.products = [
            Product("MacBook Air M2", 1450, 100),
            Product("Bose QuietComfort Earbuds", 250, 500),
            Product("Google Pixel 7", 500, 250),
            NonStockedProduct("Windows License", price=125),
            LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

        ]
        self.products[0].set_promotion(PercentageDiscount(20))
        self.products[2].set_promotion(Buy2Get1Free())
        self.products[3].set_promotion(SecondItemHalfPrice())

    def list_products(self):
        print("------")
        for idx, product in enumerate(self.products, 1):
            print(f"{idx}. {product}")
        print("------")

    def total_quantity(self):
        total = sum(product.quantity for product in self.products)
        print(f"Total of {total} items in store")

    def get_product(self, index):
        if 1 <= index <= len(self.products):
            return self.products[index - 1]
        return None
