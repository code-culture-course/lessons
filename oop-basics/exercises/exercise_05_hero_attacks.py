"""
Exercise 5: Hero Attacks Enemy ⭐⭐

Create both Hero and Enemy classes:
- Hero has: name, hp (default 10), strength (default 2)
- Enemy has: name, hp (default 5)
- Hero has an attack(enemy) method that:
  - Reduces enemy HP by hero's strength
  - Prints: "{hero_name} attacks {enemy_name} for {strength} damage!"

Example usage:
    hero = Hero("Olya")
    slime = Enemy("Slime")
    hero.attack(slime)  # Olya attacks Slime for 2 damage!
    print(slime.hp)  # 3
"""


# TODO: Define your Hero class here


# TODO: Define your Enemy class here


# Test your code
# Uncomment the code below after defining your Hero and Enemy classes
"""
if __name__ == "__main__":
    hero = Hero("Olya")
    slime = Enemy("Slime")
    
    print(f"Hero: {hero.name} (Strength: {hero.strength})")
    print(f"Enemy: {slime.name} (HP: {slime.hp})")
    print()
    
    hero.attack(slime)
    print(f"Enemy HP after attack: {slime.hp}")
    
    hero.attack(slime)
    print(f"Enemy HP after attack: {slime.hp}")
"""
