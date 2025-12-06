"""
Exercise 3: Add is_alive Property ⭐⭐

Extend your Enemy class:
- Add an is_alive() method that returns True if HP > 0, otherwise False

Example usage:
    slime = Enemy("Slime")
    print(slime.is_alive())  # True
    
    slime.take_damage(5)
    print(slime.is_alive())  # False
"""


# TODO: Define your Enemy class here


# Test your code
if __name__ == "__main__":
    slime = Enemy("Slime")
    
    print(f"Slime HP: {slime.hp}")
    print(f"Is alive: {slime.is_alive()}")
    
    slime.take_damage(3)
    print(f"Is alive: {slime.is_alive()}")
    
    slime.take_damage(2)
    print(f"Is alive: {slime.is_alive()}")
    
    slime.take_damage(1)
    print(f"Is alive: {slime.is_alive()}")
