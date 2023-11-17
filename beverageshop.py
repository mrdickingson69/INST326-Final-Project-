class BeverageShop:
  def __init__(self):
        # Input from txt file "Bev Shop", bottom methods was originally based on hardcoded menu

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
