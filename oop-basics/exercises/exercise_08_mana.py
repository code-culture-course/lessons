"""
Exercise 8: Resource System (Optional Challenge) ⭐⭐⭐⭐

Create a Mage class with a mana system:
- Attributes: name, hp (default 8), mana (default 20), max_mana (default 20)
- cast_spell(target, cost) method:
  - Only works if mana >= cost
  - Reduces mana by cost
  - Deals 3 damage to target
  - Prints spell cast message or "Not enough mana!" message
- restore_mana(amount) method (can't exceed max_mana)

Example usage:
    mage = Mage("Elena")
    enemy = Enemy("Goblin", 10)
    
    mage.cast_spell(enemy, 5)  # Works, costs 5 mana
    mage.cast_spell(enemy, 5)  # Works
    mage.cast_spell(enemy, 5)  # Works
    mage.cast_spell(enemy, 5)  # Works
    mage.cast_spell(enemy, 5)  # Fails - not enough mana
    
    mage.restore_mana(10)
    mage.cast_spell(enemy, 5)  # Works again
"""


# TODO: Define your Enemy class here (if needed)


# TODO: Define your Mage class here


# Test your code
# Uncomment the code below after defining your Mage class
"""
if __name__ == "__main__":
    from exercise_03_is_alive import Enemy  # You can import Enemy if you want
    
    mage = Mage("Elena")
    goblin = Enemy("Goblin", 15)
    
    print(f"Mage: {mage.name}")
    print(f"HP: {mage.hp}, Mana: {mage.mana}/{mage.max_mana}")
    print(f"Enemy: {goblin.name} (HP: {goblin.hp})")
    print()
    
    # Cast spells
    for i in range(5):
        print(f"--- Spell Attempt {i+1} ---")
        mage.cast_spell(goblin, 5)
        print(f"Mage mana: {mage.mana}/{mage.max_mana}")
        print()
    
    # Restore mana
    print("--- Restoring Mana ---")
    mage.restore_mana(10)
    print(f"Mage mana: {mage.mana}/{mage.max_mana}")
    print()
    
    # Cast again
    print("--- Spell After Restore ---")
    mage.cast_spell(goblin, 5)
    print(f"Enemy HP: {goblin.hp}")
"""
