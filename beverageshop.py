class BeverageShop:
    def __init__(self, menu_file="beverage_menu.txt"):
        """
        Initializes the BeverageShop instance.

        Parameters:
        - menu_file (str): The file path to the menu txt file.
        """
        self.menu = self.load_menu(menu_file)
        self.order = []

    def load_menu(self):
    # I added this menu to load the beverage_menu.txt file
    menu = {}
    with open("beverage_menu.txt", "r") as file:
        for line in file:
            name, size, price = line.strip().split(",")
            menu[name] = {"size": size, "price": float(price)}
    return menu

    def display_menu(self):
        # Display the menu of the beverage shop
        print("==== Beverage Menu ====")
        for category, sizes in self.menu.items():
            print(f"\n{category}:")
            for size, price in sizes.items():
                print(f"  {size}: ${price:.2f}")

    def place_order(self):
        """
        Allows the customer to place an order by selecting items from the menu.
        Verifies age for alcoholic beverages.

        Uses a conditional expression for age verification.
        """
        while True:
            item = input("Enter the beverage you want to order. If it's an alcohol beverage, insert 'Alcohol' (type 'done' to finish): ")
            if item.lower() == 'done':
                break
            if item.lower() == 'alcohol':
                age = int(input("Enter your age for age verification: "))
                if age < 21:
                    print("Sorry, you are not allowed to order alcoholic beverages.")
                    continue
                else:
                    print("Age verified.")
                    alcohol_type = input("Do you want Wine or Beer? ").lower()
                    if alcohol_type in ["wine", "beer"]:
                        size = input("Enter the size (e.g., small, medium, large): ")
                        quantity = int(input("Enter the quantity: "))
                        self.order.append({"item": alcohol_type, "size": size, "quantity": quantity})
                    else:
                        print("Invalid alcohol type. Please choose either Wine or Beer.")
                        continue
            elif item in self.menu:
                size = input("Enter the size (e.g., Small, Medium, Large): ")
                quantity = int(input("Enter the quantity: "))
                self.order.append({"item": item, "size": size, "quantity": quantity})
            else:
                print("Invalid beverage. Please choose from the menu.")



    def calculate_total(self):
        """
        Calculates the total cost of the customer's order.

        Returns:
        - float: The total cost of the order.

        Uses a comprehension to calculate the total cost.
        """
        total_cost = sum(self.menu[item["item"].title()][item["size"]] * item["quantity"] for item in self.order)
        return total_cost

    def display_order_summary(self):
            """
            Displays the order summary to the customer.
            """
            print("\nOrder Summary:\n")
            for item in self.order:
                print(f"{item['quantity']} {item['size']} {item['item']}")
    
            total_cost = self.calculate_total()
            print(f"\nTotal Cost: ${total_cost:.2f}")
    
        def run(self):
            """
            Executes the beverage shop application.
            """
            print("Welcome to the Beverage Shop!")
            self.display_menu()
            self.place_order()
            self.display_order_summary()
            print("\nThank you for your order!")
    
    
    if __name__ == "__main__":
        shop = BeverageShop()
        shop.run()
