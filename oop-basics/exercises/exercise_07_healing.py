"""
Exercise 7: Add Healing ⭐⭐⭐

Extend your Hero class:
- Add a max_hp attribute
- Add a heal(amount) method that:
  - Increases HP by amount
  - Doesn't let HP exceed max_hp
  - Prints: "{name} heals for {amount}! HP: {current_hp}/{max_hp}"

Example usage:
    hero = Hero("Olya")
    hero.take_damage(5)  # HP: 5/10
    hero.heal(3)         # Olya heals for 3! HP: 8/10
    hero.heal(5)         # Olya heals for 5! HP: 10/10 (capped at max)
"""


# TODO: Define your Hero class here


# Test your code
if __name__ == "__main__":
    hero = Hero("Olya")
    
    print(f"Starting HP: {hero.hp}/{hero.max_hp}")
    
    # Take damage
    hero.take_damage(5)
    print(f"After damage: {hero.hp}/{hero.max_hp}")
    
    # Heal partially
    hero.heal(3)
    
    # Try to overheal
    hero.heal(10)
    
    # Take more damage
    hero.take_damage(7)
    
    # Heal to full
    hero.heal(10)
