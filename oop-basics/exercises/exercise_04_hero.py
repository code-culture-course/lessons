"""
Exercise 4: Create a Hero Class ⭐⭐

Create a Hero class with:
- name attribute (passed in __init__)
- hp attribute (default 10)
- strength attribute (default 2)
- A greet() method that prints "Hello, I am {name}!"

Example usage:
    hero = Hero("Olya")
    hero.greet()  # Hello, I am Olya!
    print(hero.hp)  # 10
    print(hero.strength)  # 2
"""


# TODO: Define your Hero class here


# Test your code
if __name__ == "__main__":
    hero = Hero("Olya")
    hero.greet()
    
    print(f"HP: {hero.hp}")
    print(f"Strength: {hero.strength}")
    
    # Test with different hero
    hero2 = Hero("Ivan")
    hero2.greet()
