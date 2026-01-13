"""
Exercise 6: Simple Battle Round ⭐⭐⭐

Extend your Hero and Enemy classes:
- Both should have attack(target) methods
- Both should have take_damage(amount) methods
- Both should have is_alive() methods
- Create a simple battle simulation where hero and enemy take turns attacking
  until one dies

Example output:
    Olya attacks Slime for 2 damage!
    Slime HP: 3/5
    Slime attacks Olya for 1 damage!
    Olya HP: 9/10
    Olya attacks Slime for 2 damage!
    Slime HP: 1/5
    Slime attacks Olya for 1 damage!
    Olya HP: 8/10
    Olya attacks Slime for 2 damage!
    Slime HP: -1/5
    Olya wins!
"""


# TODO: Define your Hero class here


# TODO: Define your Enemy class here


# Uncomment the code below after defining your Hero and Enemy classes
"""
# Test your code
if __name__ == "__main__":
    hero = Hero("Olya")
    enemy = Enemy("Slime", 5)
    
    print("=== Battle Start ===")
    print(f"{hero.name}: {hero.hp} HP")
    print(f"{enemy.name}: {enemy.hp} HP")
    print()
    
    # Battle loop
    round_num = 1
    while hero.is_alive() and enemy.is_alive():
        print(f"--- Round {round_num} ---")
        hero.attack(enemy)
        
        if enemy.is_alive():
            enemy.attack(hero)
        
        print()
        round_num += 1
    
    # Announce winner
    if hero.is_alive():
        print(f"🎉 {hero.name} wins!")
    else:
        print(f"💀 {enemy.name} wins!")
"""
