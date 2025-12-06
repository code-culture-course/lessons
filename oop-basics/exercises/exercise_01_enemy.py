"""
Exercise 1: Create an Enemy Class ⭐

Create an Enemy class with:
- name attribute (string)
- hp attribute (integer, default 5)
- A method roar() that prints "{name} roars menacingly!"

Example usage:
    slime = Enemy("Slime")
    slime.roar()  # Slime roars menacingly!
    print(slime.hp)  # 5
"""


# TODO: Define your Enemy class here


# Test your code
if __name__ == "__main__":
    slime = Enemy("Slime")
    print(f"Name: {slime.name}")
    print(f"HP: {slime.hp}")
    slime.roar()
    
    # Test with different enemy
    goblin = Enemy("Goblin")
    goblin.roar()
