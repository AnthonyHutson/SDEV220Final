class WingMenu:
    def __init__(self):
        # Initialize the wing menu with available wings and their prices
        self.menu = {
            "Buffalo Wings": 7.99,
            "BBQ Wings": 8.49,
            "Garlic Parmesan Wings": 8.99,
            "Honey Mustard Wings": 7.49,
            "Spicy Asian Wings": 9.49
        }

    def display_menu(self):
        """Display the wing menu with their prices"""
        print("Wing Menu:")
        for wing, price in self.menu.items():
            print(f"{wing}: ${price:.2f}")

    def add_wing(self, name, price):
        """Add a new wing flavor to the menu"""
        if name in self.menu:
            print(f"{name} is already on the menu.")
        else:
            self.menu[name] = price
            print(f"{name} added to the menu.")

    def remove_wing(self, name):
        """Remove a wing flavor from the menu"""
        if name in self.menu:
            del self.menu[name]
            print(f"{name} removed from the menu.")
        else:
            print(f"{name} not found on the menu.")

    def update_price(self, name, new_price):
        """Update the price of an existing wing flavor"""
        if name in self.menu:
            self.menu[name] = new_price
            print(f"Price for {name} updated to ${new_price:.2f}.")
        else:
            print(f"{name} not found on the menu.")

    def get_price(self, name):
        """Get the price of a wing flavor"""
        if name in self.menu:
            return f"The price of {name} is ${self.menu[name]:.2f}."
        else:
            return f"{name} not found on the menu."


# Example usage:
menu = WingMenu()
menu.display_menu()

# Add a new wing flavor
menu.add_wing("Lemon Pepper Wings", 8.99)

# Remove a wing flavor
menu.remove_wing("Honey Mustard Wings")

# Update wing flavor price
menu.update_price("BBQ Wings", 8.99)

# Get the price of a wing flavor
print(menu.get_price("Buffalo Wings"))
