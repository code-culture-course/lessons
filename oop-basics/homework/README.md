# OOP Homework: RPG Classes

## Overview

In this homework assignment, you'll create a small RPG (Role-Playing Game) system using Object-Oriented Programming principles. You'll implement three main classes that work together to model game items, inventories, and heroes.

## Learning Objectives

By completing this homework, you will:
- Practice defining classes with `__init__` methods
- Work with object attributes and methods
- Create objects that interact with each other
- Manage collections of objects
- Build a cohesive system from multiple classes

## Submission Requirements

1. Create a file named `rpg_classes.py` in this directory
2. Implement all required classes and methods
3. Add test code at the bottom demonstrating functionality
4. Ensure your code runs without errors
5. Commit with message: `feat: complete OOP homework - RPG classes`
6. Submit according to your instructor's guidelines

---

## Part 1: Item Class ⭐⭐

Create an `Item` class that represents items in an RPG (swords, potions, keys, etc.).

### Requirements

**Attributes:**
- `name` (string) - the item's name
- `description` (string) - a description of the item
- `value` (integer) - the item's value in gold

**Methods:**
- `describe()` - prints: `"{name}: {description} (Value: {value} gold)"`

### Example Usage

```python
sword = Item("Iron Sword", "A sturdy blade", 50)
sword.describe()
# Output: Iron Sword: A sturdy blade (Value: 50 gold)

print(sword.name)   # Iron Sword
print(sword.value)  # 50

potion = Item("Health Potion", "Restores 5 HP", 10)
potion.describe()
# Output: Health Potion: Restores 5 HP (Value: 10 gold)
```

### Acceptance Criteria

✅ Item objects can be created with name, description, and value  
✅ `describe()` method prints correctly formatted string  
✅ Attributes can be accessed directly  

---

## Part 2: Inventory System ⭐⭐⭐

Create an `Inventory` class that manages a collection of items.

### Requirements

**Attributes:**
- `items` (list) - a list of Item objects, initially empty

**Methods:**
- `add_item(item)` - adds an Item object to the inventory
- `remove_item(item_name)` - removes the first item with matching name (if it exists)
- `list_items()` - prints all items in the inventory in a formatted list
- `total_value()` - returns the sum of all item values

### Example Usage

```python
inventory = Inventory()

# Add items
inventory.add_item(Item("Potion", "Restores 5 HP", 10))
inventory.add_item(Item("Sword", "A sharp blade", 50))
inventory.add_item(Item("Key", "Opens doors", 5))

# List items
inventory.list_items()
# Output:
# Inventory:
# - Potion: Restores 5 HP (Value: 10 gold)
# - Sword: A sharp blade (Value: 50 gold)
# - Key: Opens doors (Value: 5 gold)

# Check total value
print(f"Total value: {inventory.total_value()} gold")
# Output: Total value: 65 gold

# Remove an item
inventory.remove_item("Potion")
inventory.list_items()
# Output:
# Inventory:
# - Sword: A sharp blade (Value: 50 gold)
# - Key: Opens doors (Value: 5 gold)

print(f"Total value: {inventory.total_value()} gold")
# Output: Total value: 55 gold
```

### Acceptance Criteria

✅ Inventory starts with an empty list  
✅ `add_item()` correctly adds items  
✅ `remove_item()` removes items by name  
✅ `list_items()` prints formatted inventory  
✅ `total_value()` correctly calculates sum  
✅ Handles empty inventory gracefully  

### Implementation Hints

- For `list_items()`: loop through `self.items` and call each item's `describe()` method
- For `remove_item()`: use a loop to find the item by name, then use `list.remove()`
- For `total_value()`: use a loop or `sum()` to add up all item values

---

## Part 3: Complete Hero Class ⭐⭐⭐

Create a full-featured `Hero` class that has attributes, methods, and an inventory.

### Requirements

**Attributes:**
- `name` (string) - hero's name
- `hp` (integer) - current hit points, default 10
- `max_hp` (integer) - maximum hit points, default 10
- `strength` (integer) - attack power, default 2
- `inventory` (Inventory object) - hero's inventory

**Methods:**
- `attack(target)` - deals `strength` damage to target
- `take_damage(amount)` - reduces HP by amount
- `heal(amount)` - increases HP (capped at max_hp)
- `is_alive()` - returns True if HP > 0
- `pick_up_item(item)` - adds item to hero's inventory
- `show_status()` - prints hero's stats and inventory

### Example Usage

```python
hero = Hero("Olya")

# Pick up items
hero.pick_up_item(Item("Health Potion", "Restores 5 HP", 10))
hero.pick_up_item(Item("Iron Key", "Opens iron doors", 5))
hero.pick_up_item(Item("Rusty Sword", "An old weapon", 15))

# Show full status
hero.show_status()
# Output:
# === Hero: Olya ===
# HP: 10/10
# Strength: 2
# Status: Alive
# 
# Inventory:
# - Health Potion: Restores 5 HP (Value: 10 gold)
# - Iron Key: Opens iron doors (Value: 5 gold)
# - Rusty Sword: An old weapon (Value: 15 gold)
# Total value: 30 gold

# Take damage
hero.take_damage(6)
hero.show_status()
# Output shows HP: 4/10

# Heal
hero.heal(3)
# Output shows HP: 7/10

# Check if alive
print(hero.is_alive())  # True
```

### Acceptance Criteria

✅ Hero created with correct default values  
✅ Hero has an Inventory object  
✅ `attack()`, `take_damage()`, `heal()` work correctly  
✅ `heal()` doesn't exceed max_hp  
✅ `is_alive()` returns correct boolean  
✅ `pick_up_item()` adds items to inventory  
✅ `show_status()` displays all information clearly  

### Implementation Hints

For `show_status()`:
```python
def show_status(self):
    print(f"=== Hero: {self.name} ===")
    print(f"HP: {self.hp}/{self.max_hp}")
    print(f"Strength: {self.strength}")
    print(f"Status: {'Alive' if self.is_alive() else 'Dead'}")
    print()
    self.inventory.list_items()
```

---

## Complete Test Code

At the bottom of your `rpg_classes.py` file, add comprehensive test code:

```python
if __name__ == "__main__":
    print("=== Testing Item Class ===")
    sword = Item("Iron Sword", "A sturdy blade", 50)
    sword.describe()
    
    print("\n=== Testing Inventory Class ===")
    inventory = Inventory()
    inventory.add_item(Item("Potion", "Restores 5 HP", 10))
    inventory.add_item(Item("Key", "Opens doors", 5))
    inventory.list_items()
    print(f"Total value: {inventory.total_value()} gold")
    
    print("\n=== Testing Hero Class ===")
    hero = Hero("Olya")
    hero.pick_up_item(Item("Health Potion", "Restores 5 HP", 10))
    hero.pick_up_item(Item("Rusty Sword", "An old weapon", 15))
    hero.show_status()
    
    print("\n=== Testing Combat ===")
    hero.take_damage(6)
    hero.show_status()
    
    hero.heal(3)
    hero.show_status()
    
    print("\n=== All tests complete! ===")
```

---

## Bonus Challenge: Merchant Class (Optional) ⭐⭐⭐⭐

Want an extra challenge? Implement a trading system!

### Requirements

Create a `Merchant` class:
- Attribute: `inventory` (Inventory object with items for sale)
- Attribute: `gold` (integer, merchant's money)
- Method: `sell_to(hero, item_name, price)` - hero buys item if they have enough gold
- Method: `buy_from(hero, item_name, price)` - merchant buys item from hero

Extend `Hero` class:
- Add `gold` attribute (default 50)
- Implement buying/selling logic

### Example Usage

```python
merchant = Merchant("Shopkeeper", gold=100)
merchant.inventory.add_item(Item("Magic Sword", "A powerful blade", 100))
merchant.inventory.add_item(Item("Shield", "Provides defense", 50))

hero = Hero("Olya")
hero.gold = 75

# Hero buys shield
merchant.sell_to(hero, "Shield", 50)
print(f"Hero gold: {hero.gold}")  # 25

# Hero sells something
hero.pick_up_item(Item("Old Boot", "Smelly", 5))
merchant.buy_from(hero, "Old Boot", 5)
print(f"Hero gold: {hero.gold}")  # 30
```

This is completely optional but great practice!

---

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| Item class correctly implemented | 20 |
| Inventory class correctly implemented | 30 |
| Hero class correctly implemented | 40 |
| Test code demonstrates all functionality | 10 |
| **Total** | **100** |

**Bonus:** Merchant class implementation: +20 points

---

## Tips for Success

1. **Work incrementally**: Complete Part 1, test it, then move to Part 2
2. **Test frequently**: Run your code after each method you add
3. **Read error messages**: They tell you exactly what's wrong
4. **Review examples**: Look at the examples in the `examples/` directory
5. **Ask questions**: Don't hesitate to ask for help if you're stuck

---

## Common Mistakes to Avoid

❌ Forgetting `self` parameter in methods  
❌ Forgetting to use `self.` when accessing attributes  
❌ Not initializing `inventory` in `Hero.__init__()`  
❌ Forgetting to cap healing at `max_hp`  
❌ Not handling empty inventories in `list_items()`  

---

Good luck! Remember, the goal is to practice OOP concepts, so focus on understanding how objects work together rather than making it perfect. 🚀
