from store import Store



class Menu:
    def __init__(self):
        self.store = Store()

    def display_menu(self):
        print("\n   Store Menu\n   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

    def make_order(self):
        self.store.list_products()
        order_total = 0
        while True:
            try:
                product_number = input("Which product # do you want? ")
                if product_number == "":
                    break
                product_number = int(product_number)
                product = self.store.get_product(product_number)
                if not product:
                    print("Invalid product number. Try again.")
                    continue

                amount = input("What amount do you want? ")
                if amount == "":
                    break
                amount = int(amount)

                if product.reduce_quantity(amount):
                    order_total += product.price * amount
                    print("Product added to list!")
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        print("********")
        print(f"Order made! Total payment: ${order_total}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Please choose a number: ")
            if choice == "1":
                self.store.list_products()
            elif choice == "2":
                self.store.total_quantity()
            elif choice == "3":
                self.make_order()
            elif choice == "4":
                print("Exiting store. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    menu = Menu()
    menu.run()
