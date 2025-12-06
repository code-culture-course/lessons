"""
OOP-based Hero System (After Learning OOP)

This is the improved version using classes and objects.

Benefits of this approach:
✅ Structure is enforced (no typos, guaranteed attributes)
✅ Data and behavior bundled together
✅ Clear interface (easy to see what objects can do)
✅ Self-documenting code
✅ Easier to extend and maintain
"""


class Hero:
    """Represents a player character"""
    
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.max_hp = 10
        self.strength = 2
    
    def attack(self, target):
        """Attack a target, dealing damage equal to strength"""
        print(f"{self.name} attacks {target.name} for {self.strength} damage!")
        target.take_damage(self.strength)
    
    def take_damage(self, amount):
        """Take damage, reducing HP"""
        self.hp -= amount
        print(f"{self.name} HP: {self.hp}/{self.max_hp}")
    
    def is_alive(self):
        """Check if hero is still alive"""
        return self.hp > 0


class Enemy:
    """Represents an enemy character"""
    
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
    
    def attack(self, target):
        """Attack a target with base damage of 1"""
        damage = 1
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
    
    def take_damage(self, amount):
        """Take damage, reducing HP"""
        self.hp -= amount
        print(f"{self.name} HP: {self.hp}/{self.max_hp}")
    
    def is_alive(self):
        """Check if enemy is still alive"""
        return self.hp > 0


def main():
    print("=== OOP-Based RPG System ===\n")
    
    # Create characters
    hero = Hero("Olya")
    enemy = Enemy("Slime", 5)
    
    print(f"Hero: {hero.name} (HP: {hero.hp})")
    print(f"Enemy: {enemy.name} (HP: {enemy.hp})")
    print()
    
    # Battle loop
    round_number = 1
    while hero.is_alive() and enemy.is_alive():
        print(f"--- Round {round_number} ---")
        hero.attack(enemy)
        
        if enemy.is_alive():
            enemy.attack(hero)
        
        print()
        round_number += 1
    
    # Determine winner
    if hero.is_alive():
        print(f"🎉 {hero.name} wins!")
    else:
        print(f"💀 {enemy.name} wins!")


if __name__ == "__main__":
    main()
