"""
Exercise 2: Add take_damage Method ⭐

Extend the Enemy class from Exercise 1:
- Add a take_damage(amount) method that reduces HP by amount
- The method should print: "{name} takes {amount} damage! HP: {current_hp}"

Example usage:
    slime = Enemy("Slime")
    slime.take_damage(2)  # Slime takes 2 damage! HP: 3
    slime.take_damage(1)  # Slime takes 1 damage! HP: 2
"""


# TODO: Define your Enemy class here


# Test your code
if __name__ == "__main__":
    slime = Enemy("Slime")
    print(f"Starting HP: {slime.hp}")
    
    slime.take_damage(2)
    slime.take_damage(1)
    slime.take_damage(2)
    
    print(f"Final HP: {slime.hp}")
