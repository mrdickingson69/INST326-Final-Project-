class BeverageShop:
    def __init__(self):
      self.menu = self.load_menu()
      self.order = []

    def display_menu(self):
        # Display the menu of the beverage shop
        print("==== Beverage Menu ====")
        for category, sizes in self.menu.items():
            print(f"\n{category}:")
            for size, price in sizes.items():
                print(f"  {size}: ${price:.2f}")

    def get_customer_age(self):
        # Get the customers age to see if they're above or below the age of 21
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
