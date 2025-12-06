"""
Example 2: Adding Methods

This example demonstrates:
- How to add methods to a class
- How self works
- How to call methods on objects
- How methods can modify object state
"""


class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.strength = 2
    
    def introduce(self):
        """Print a greeting message"""
        print(f"I am {self.name}, and I have {self.hp} HP!")
    
    def take_damage(self, amount):
        """Reduce HP by the given amount"""
        self.hp -= amount
        print(f"{self.name} took {amount} damage! HP now: {self.hp}")


if __name__ == "__main__":
    # Create a hero
    hero = Hero("Olya")
    
    # Call methods
    hero.introduce()
    # Output: I am Olya, and I have 10 HP!
    
    hero.take_damage(3)
    # Output: Olya took 3 damage! HP now: 7
    
    hero.introduce()
    # Output: I am Olya, and I have 7 HP!
