"""
Homework Template: RPG Classes

Complete the implementation of the three classes below.
Follow the requirements in the homework README.md file.

Delete the 'pass' statements and add your implementation.
"""


class Item:
    """Represents an item in the RPG"""
    
    def __init__(self, name, description, value):
        # TODO: Initialize attributes
        pass
    
    def describe(self):
        """Print item description"""
        # TODO: Implement this method
        pass


class Inventory:
    """Manages a collection of items"""
    
    def __init__(self):
        # TODO: Initialize empty items list
        pass
    
    def add_item(self, item):
        """Add an item to the inventory"""
        # TODO: Implement this method
        pass
    
    def remove_item(self, item_name):
        """Remove an item by name"""
        # TODO: Implement this method
        pass
    
    def list_items(self):
        """Print all items in inventory"""
        # TODO: Implement this method
        pass
    
    def total_value(self):
        """Return sum of all item values"""
        # TODO: Implement this method
        pass


class Hero:
    """Represents a hero character"""
    
    def __init__(self, name):
        # TODO: Initialize all attributes including Inventory
        pass
    
    def attack(self, target):
        """Attack a target"""
        # TODO: Implement this method
        pass
    
    def take_damage(self, amount):
        """Take damage, reducing HP"""
        # TODO: Implement this method
        pass
    
    def heal(self, amount):
        """Heal, increasing HP (capped at max_hp)"""
        # TODO: Implement this method
        pass
    
    def is_alive(self):
        """Check if hero is alive"""
        # TODO: Implement this method
        pass
    
    def pick_up_item(self, item):
        """Add item to inventory"""
        # TODO: Implement this method
        pass
    
    def show_status(self):
        """Display hero stats and inventory"""
        # TODO: Implement this method
        pass


# Test your code here
if __name__ == "__main__":
    print("=== Testing Item Class ===")
    # Add your test code
    
    print("\n=== Testing Inventory Class ===")
    # Add your test code
    
    print("\n=== Testing Hero Class ===")
    # Add your test code
    
    print("\n=== All tests complete! ===")
