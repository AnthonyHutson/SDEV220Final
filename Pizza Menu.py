class PizzaMenu:
    def __init__(self):
        # Initialize the pizza menu with available pizzas and their prices
        self.menu = {
            "Margherita": 8.99,
            "Pepperoni": 9.99,
            "Vegetarian": 10.99,
            "BBQ Chicken": 11.99,
            "Hawaiian": 10.49
        }

    def display_menu(self):
        """Display the pizza menu with their prices"""
        print("Pizza Menu:")
        for pizza, price in self.menu.items():
            print(f"{pizza}: ${price:.2f}")

    def add_pizza(self, name, price):
        """Add a new pizza to the menu"""
        if name in self.menu:
            print(f"{name} is already on the menu.")
        else:
            self.menu[name] = price
            print(f"{name} added to the menu.")

    def remove_pizza(self, name):
        """Remove a pizza from the menu"""
        if name in self.menu:
            del self.menu[name]
            print(f"{name} removed from the menu.")
        else:
            print(f"{name} not found on the menu.")

    def update_price(self, name, new_price):
        """Update the price of an existing pizza"""
        if name in self.menu:
            self.menu[name] = new_price
            print(f"Price for {name} updated to ${new_price:.2f}.")
        else:
            print(f"{name} not found on the menu.")

    def get_price(self, name):
        """Get the price of a pizza"""
        if name in self.menu:
            return f"The price of {name} is ${self.menu[name]:.2f}."
        else:
            return f"{name} not found on the menu."


# Example usage:
menu = PizzaMenu()
menu.display_menu()

# Add a new pizza
menu.add_pizza("Four Cheese", 12.99)

# Remove a pizza
menu.remove_pizza("Hawaiian")

# Update pizza price
menu.update_price("Pepperoni", 10.49)

# Get the price of a pizza
print(menu.get_price("Margherita"))
