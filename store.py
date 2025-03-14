from products import Product

class Store:
    def __init__(self):
        self.products = [
            Product("MacBook Air M2", 1450, 100),
            Product("Bose QuietComfort Earbuds", 250, 500),
            Product("Google Pixel 7", 500, 250)
        ]

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
