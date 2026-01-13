"""
Example 1: Basic Class Definition

This example shows the most basic class structure:
- How to define a class
- How to create an __init__ method
- How to set attributes
- How to create objects (instances)
"""


class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.strength = 2


if __name__ == "__main__":
    # Create a hero
    hero = Hero("Olya")
    
    # Access attributes
    print(f"Name: {hero.name}")
    print(f"HP: {hero.hp}")
    print(f"Strength: {hero.strength}")
    
    # Modify attributes
    hero.hp = 8
    print(f"HP after taking damage: {hero.hp}")
