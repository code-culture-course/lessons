"""
Example 4: Objects Interacting

This example demonstrates:
- How objects can interact with each other
- Methods can accept other objects as parameters
- Objects can call methods on other objects
"""


class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.strength = 2
    
    def attack(self, enemy):
        """Attack an enemy, dealing damage equal to strength"""
        print(f"{self.name} attacks {enemy.name}!")
        enemy.take_damage(self.strength)
    
    def take_damage(self, amount):
        """Take damage, reducing HP"""
        self.hp -= amount
        print(f"{self.name} took {amount} damage! HP: {self.hp}")


class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def take_damage(self, amount):
        """Take damage, reducing HP"""
        self.hp -= amount
        print(f"{self.name} took {amount} damage! HP: {self.hp}")


if __name__ == "__main__":
    # Create characters
    hero = Hero("Olya")
    enemy = Enemy("Slime", 5)
    
    print("=== Combat Start ===")
    
    # Hero attacks enemy multiple times
    hero.attack(enemy)
    # Output:
    # Olya attacks Slime!
    # Slime took 2 damage! HP: 3
    
    hero.attack(enemy)
    # Output:
    # Olya attacks Slime!
    # Slime took 2 damage! HP: 1
    
    hero.attack(enemy)
    # Output:
    # Olya attacks Slime!
    # Slime took 2 damage! HP: -1
    
    print(f"\nFinal HP - Hero: {hero.hp}, Enemy: {enemy.hp}")
