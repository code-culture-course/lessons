"""
Example 3: Multiple Objects

This example shows:
- How to create multiple instances of a class
- Each instance has its own independent state
- Modifying one object doesn't affect others
"""


class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
    
    def show_status(self):
        print(f"{self.name}: {self.hp} HP")


if __name__ == "__main__":
    # Create multiple heroes
    hero1 = Hero("Olya")
    hero2 = Hero("Ivan")
    hero3 = Hero("Maria")
    
    # Show initial state
    print("Initial state:")
    hero1.show_status()  # Olya: 10 HP
    hero2.show_status()  # Ivan: 10 HP
    hero3.show_status()  # Maria: 10 HP
    
    # Modify some heroes
    hero1.hp = 5
    hero2.hp = 8
    # hero3.hp remains unchanged
    
    # Show modified state
    print("\nAfter modifications:")
    hero1.show_status()  # Olya: 5 HP
    hero2.show_status()  # Ivan: 8 HP
    hero3.show_status()  # Maria: 10 HP (unchanged!)
