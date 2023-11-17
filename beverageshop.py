class BeverageShop:
    def __init__(self):
        self.menu = {
            'Coffee': {'Small': 2.50, 'Medium': 3.00, 'Large': 3.50},
            'Tea': {'Small': 2.00, 'Medium': 2.50, 'Large': 3.00},
            'Smoothie': {'Small': 4.00, 'Medium': 4.50, 'Large': 5.00},
            'Beer': {'Small': 5.00, 'Medium': 6.00, 'Large': 7.00},
            'Wine': {'Small': 6.00, 'Medium': 7.00, 'Large': 8.00}
        }
        self.order = []

    def display_menu(self):
        print("==== Beverage Menu ====")
        for category, sizes in self.menu.items():
            print(f"\n{category}:")
            for size, price in sizes.items():
                print(f"  {size}: ${price:.2f}")

    def get_customer_age(self):
        try:
            age = int(input("Please enter your age for age verification: "))
            return age
        except ValueError:
            print("Invalid input. Please enter a valid age.")
            return self.get_customer_age()

    def place_order(self):
        self.display_menu()
        while True:
            beverage = input("\nEnter the name of the beverage you'd like to order (or 'done' to finish): ").capitalize()
            if beverage == 'Done':
                break
            elif beverage in self.menu:
                size = input("Select size (Small, Medium, Large): ").capitalize()
                if size not in self.menu[beverage]:
                    print("Invalid size. Please choose a valid size.")
                    continue
                quantity = int(input("Enter quantity: "))
                self.order.append({'beverage': beverage, 'size': size, 'quantity': quantity})
            else:
                print("Invalid beverage. Please choose a beverage from the menu.")

    def calculate_total(self):
        total_cost = 0.0
        for item in self.order:
            beverage = item['beverage']
            size = item['size']
            quantity = item['quantity']
            price = self.menu[beverage][size]
            total_cost += price * quantity
        return total_cost

    def main(self):
        print("Welcome to the Beverage Shop!")
        self.place_order()

        for item in self.order:
            beverage = item['beverage']
            if beverage in ['Beer', 'Wine']:
                age = self.get_customer_age()
                if age < 21:
                    print("Sorry, you cannot order alcohol. Thank you for your understanding.")
                    return

        total_cost = self.calculate_total()
        print(f"\nYour order total is: ${total_cost:.2f}")
        print("Thank you for ordering at the Beverage Shop!")


if __name__ == "__main__":
    beverage_shop = BeverageShop()
    beverage_shop.main()

