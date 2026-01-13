"""
Dictionary-based Hero System (Before OOP)

This example shows the old way of modeling game characters
using dictionaries and standalone functions.

Problems with this approach:
- No structure enforcement (typos can break things)
- Functions and data are separate
- Hard to ensure consistency
- No clear interface
- Global functions scattered everywhere
"""


def create_hero(name):
    """Create a hero dictionary"""
    return {
        "name": name,
        "hp": 10,
        "max_hp": 10,
        "strength": 2
    }


def create_enemy(name, hp):
    """Create an enemy dictionary"""
    return {
        "name": name,
        "hp": hp,
        "max_hp": hp
    }


def attack(attacker, target):
    """One character attacks another"""
    damage = attacker.get("strength", 1)
    target["hp"] -= damage
    print(f"{attacker['name']} attacks {target['name']} for {damage} damage!")
    print(f"{target['name']} HP: {target['hp']}/{target['max_hp']}")


def is_alive(character):
    """Check if a character is alive"""
    return character["hp"] > 0


def main():
    print("=== Dictionary-Based RPG System ===\n")
    
    # Create characters
    hero = create_hero("Olya")
    enemy = create_enemy("Slime", 5)
    
    print(f"Hero: {hero['name']} (HP: {hero['hp']})")
    print(f"Enemy: {enemy['name']} (HP: {enemy['hp']})")
    print()
    
    # Battle loop
    round_number = 1
    while is_alive(hero) and is_alive(enemy):
        print(f"--- Round {round_number} ---")
        attack(hero, enemy)
        
        if is_alive(enemy):
            attack(enemy, hero)
        
        print()
        round_number += 1
    
    # Determine winner
    if is_alive(hero):
        print(f"🎉 {hero['name']} wins!")
    else:
        print(f"💀 {enemy['name']} wins!")


if __name__ == "__main__":
    main()
