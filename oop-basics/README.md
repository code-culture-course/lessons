# Object-Oriented Programming in Python

## Lesson Overview

Welcome to the Object-Oriented Programming (OOP) module! This lesson introduces one of the most important programming paradigms for building larger, more organized applications.

**Where we are in the learning path:**

So far, you've learned:
- Python basics (variables, loops, conditionals)
- Functions (breaking code into reusable pieces)
- Modules (organizing functions into files)
- Testing (ensuring code works correctly)
- Small CLI projects (bringing it all together)

Now you're ready for the next step: **organizing code around objects** rather than just functions.

**Why OOP matters:**

As programs grow, organizing code with just functions and dictionaries becomes messy. OOP provides a better way to structure your code by bundling data and behavior together. This makes your programs:

- Easier to understand
- Easier to extend
- Easier to maintain
- More natural when modeling real-world concepts

Whether you're building games, web applications, or data processing tools, OOP will help you write cleaner, more organized code.

---

## Historical Background: Why OOP Exists

### The Problem with Procedural Programming

In the early days, programs were written procedurally—just functions operating on data. This worked fine for small programs, but as software grew, developers hit serious problems:

**1. Data and behavior were scattered everywhere**

Imagine modeling a hero in a game using just functions and dictionaries:

```python
hero = {"name": "Olya", "hp": 10, "strength": 5}

def attack(attacker, target):
    target["hp"] -= attacker["strength"]

def heal(character, amount):
    character["hp"] += amount
```

Where is all the hero logic? It's spread across multiple functions. When you need to understand how heroes work, you have to hunt through the entire codebase.

**2. No structure binding data and functions together**

Nothing prevents you from writing:

```python
hero = {"name": "Olya", "hp": 10}
enemy = {"name": "Slime", "health": 5}  # Oops! Used "health" instead of "hp"

attack(hero, enemy)  # This might crash!
```

There's no enforcement that hero dictionaries must have certain keys, or that certain functions work with certain data structures.

**3. Global mutable state everywhere**

```python
all_heroes = []
hero_count = 0

def create_hero(name):
    global hero_count
    hero_count += 1
    hero = {"name": name, "id": hero_count, "hp": 10}
    all_heroes.append(hero)
    return hero
```

Functions accessing global variables make code hard to reason about. Who modifies `hero_count`? Who reads it? It's unclear.

**4. Difficulty modeling real-world concepts**

When you think about a game, you naturally think: "I have heroes, enemies, items, and quests." But with procedural code, you end up with:

```python
hero_names = []
hero_hp = []
hero_strength = []

def get_hero_hp(hero_index):
    return hero_hp[hero_index]
```

This doesn't match how we think about the problem. A hero should be a cohesive thing, not data scattered across multiple lists.

**5. Error-prone code**

```python
hero = {"name": "Olya", "hp": 10}
hero["helth"] -= 1  # Typo! Python won't catch this until runtime
```

Dictionaries don't protect you from typos or structural mistakes.

### How OOP Solved These Problems

Object-Oriented Programming emerged to address these exact issues:

**1. Encapsulation: Data lives with behavior**

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
    
    def attack(self, enemy):
        enemy.hp -= 1
    
    def heal(self, amount):
        self.hp += amount
```

Now all hero-related logic lives in one place. Want to know what heroes can do? Look at the `Hero` class.

**2. Clear structure and contracts**

Every `Hero` instance is guaranteed to have a `name` and `hp` attribute. No more guessing or runtime surprises.

**3. Better modularity**

```python
hero = Hero("Olya")
enemy = Enemy("Slime")
hero.attack(enemy)
```

Each object manages its own state. No global variables needed.

**4. Natural domain modeling**

OOP lets you model your problem domain directly:
- Heroes ARE objects
- Enemies ARE objects
- Items ARE objects

This matches how humans think about the world.

**5. Clearer reasoning about state**

When you call `hero.heal(5)`, you know exactly what's affected: this specific hero instance. No hidden global state to worry about.

---

## Core Concepts

### What is a Class?

A **class** is a blueprint or template for creating objects. Think of it like a cookie cutter—it defines the shape, but it's not the cookie itself.

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
```

The `Hero` class defines:
- What data every hero has (`name` and `hp`)
- What behavior every hero has (we'll add methods soon)

### What is an Object (Instance)?

An **object** (or **instance**) is a concrete example created from a class. Using our cookie cutter analogy, an object is the actual cookie.

```python
hero1 = Hero("Olya")    # One hero
hero2 = Hero("Ivan")    # Another hero
```

`hero1` and `hero2` are separate objects. They're both heroes, but they have different names and can have different HP values.

### What are Attributes?

**Attributes** are the data that belong to an object. They describe the object's state.

```python
class Hero:
    def __init__(self, name):
        self.name = name  # 'name' is an attribute
        self.hp = 10      # 'hp' is an attribute
```

Each hero has its own `name` and `hp`. When you change one hero's HP, other heroes aren't affected:

```python
hero1 = Hero("Olya")
hero2 = Hero("Ivan")

hero1.hp = 5  # Only hero1 is affected
print(hero2.hp)  # Still 10
```

### What are Methods?

**Methods** are functions that belong to a class. They define what objects can DO.

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
    
    def take_damage(self, amount):  # This is a method
        self.hp -= amount
        print(f"{self.name} took {amount} damage! HP: {self.hp}")
```

Methods are called on specific objects:

```python
hero = Hero("Olya")
hero.take_damage(3)  # Calls the method on this specific hero
```

### What is `__init__`?

`__init__` is a special method called the **constructor** or **initializer**. It runs automatically when you create a new object.

```python
class Hero:
    def __init__(self, name):
        # This runs when you write: hero = Hero("Olya")
        self.name = name
        self.hp = 10
        print(f"Hero {name} has been created!")

hero = Hero("Olya")  # Prints: "Hero Olya has been created!"
```

Use `__init__` to:
- Set up initial attribute values
- Perform any setup needed when an object is created

### What is `self`?

`self` refers to "this specific object." It's how methods access the object's own attributes and other methods.

```python
class Hero:
    def __init__(self, name):
        self.name = name  # "Store 'name' in THIS hero's 'name' attribute"
        self.hp = 10
    
    def introduce(self):
        print(f"I am {self.name}")  # "Access THIS hero's 'name' attribute"
```

When you call `hero.introduce()`, Python automatically passes `hero` as the `self` parameter.

**Important:** `self` is just a naming convention. You could technically name it anything, but everyone uses `self`, so you should too.

### Encapsulation (Introduction)

**Encapsulation** means bundling data (attributes) and behavior (methods) together in a single unit (the class).

Instead of:
```python
# Data here
hero_data = {"name": "Olya", "hp": 10}

# Behavior somewhere else
def hero_attack(hero, enemy):
    # ...
```

You have:
```python
class Hero:
    def __init__(self, name):
        self.name = name  # Data
        self.hp = 10
    
    def attack(self, enemy):  # Behavior
        # ...
```

Everything related to heroes is in one place. This makes code easier to understand, test, and modify.

### Why OOP Fits Naturally for Games

When building a game, you naturally think in terms of entities:

- **Heroes** have health, strength, and can attack
- **Enemies** have health, AI behavior, and can fight back
- **Items** have names, effects, and can be used
- **Quests** have objectives, rewards, and completion status

OOP lets you model these entities directly:

```python
class Hero:
    # Hero stuff

class Enemy:
    # Enemy stuff

class Item:
    # Item stuff
```

This matches your mental model of the game world, making code intuitive to read and write.

---

## Code Examples

### Example 1: Basic Class Definition

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.strength = 2

# Create a hero
hero = Hero("Olya")
print(hero.name)      # Olya
print(hero.hp)        # 10
print(hero.strength)  # 2
```

### Example 2: Adding Methods

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.strength = 2
    
    def introduce(self):
        print(f"I am {self.name}, and I have {self.hp} HP!")
    
    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} took {amount} damage! HP now: {self.hp}")

# Using methods
hero = Hero("Olya")
hero.introduce()           # I am Olya, and I have 10 HP!
hero.take_damage(3)        # Olya took 3 damage! HP now: 7
hero.introduce()           # I am Olya, and I have 7 HP!
```

### Example 3: Multiple Objects

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10

# Create multiple heroes
hero1 = Hero("Olya")
hero2 = Hero("Ivan")
hero3 = Hero("Maria")

# Each has their own state
hero1.hp = 5
hero2.hp = 8

print(hero1.hp)  # 5
print(hero2.hp)  # 8
print(hero3.hp)  # 10 (unchanged)
```

### Example 4: Objects Interacting

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.strength = 2
    
    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        enemy.take_damage(self.strength)
    
    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} took {amount} damage! HP: {self.hp}")

class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} took {amount} damage! HP: {self.hp}")

# Combat!
hero = Hero("Olya")
enemy = Enemy("Slime", 5)

hero.attack(enemy)  # Olya attacks Slime!
                    # Slime took 2 damage! HP: 3
hero.attack(enemy)  # Olya attacks Slime!
                    # Slime took 2 damage! HP: 1
```

### Example 5: Computed Properties

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.max_hp = 10
    
    def is_alive(self):
        return self.hp > 0
    
    def hp_percentage(self):
        return (self.hp / self.max_hp) * 100
    
    def status(self):
        if self.hp == self.max_hp:
            return "healthy"
        elif self.hp > self.max_hp / 2:
            return "wounded"
        elif self.hp > 0:
            return "critical"
        else:
            return "dead"

hero = Hero("Olya")
print(hero.is_alive())      # True
print(hero.hp_percentage()) # 100.0
print(hero.status())        # healthy

hero.hp = 3
print(hero.hp_percentage()) # 30.0
print(hero.status())        # critical
```

---

## Step-by-Step Mini-Project: From Dictionaries to Classes

### Step 1: The Dictionary Approach

Let's start with how you might have built a simple RPG system before learning OOP:

```python
# hero_dict_version.py
def create_hero(name):
    return {
        "name": name,
        "hp": 10,
        "max_hp": 10,
        "strength": 2
    }

def create_enemy(name, hp):
    return {
        "name": name,
        "hp": hp,
        "max_hp": hp
    }

def attack(attacker, target):
    damage = attacker["strength"]
    target["hp"] -= damage
    print(f"{attacker['name']} attacks {target['name']} for {damage} damage!")
    print(f"{target['name']} HP: {target['hp']}/{target['max_hp']}")

def is_alive(character):
    return character["hp"] > 0

# Using the system
hero = create_hero("Olya")
enemy = create_enemy("Slime", 5)

while is_alive(hero) and is_alive(enemy):
    attack(hero, enemy)
    if is_alive(enemy):
        attack(enemy, hero)
```

This works, but let's look at the problems...

### Step 2: Problems with the Dictionary Approach

**Problem 1: No structure enforcement**

```python
hero = create_hero("Olya")
# Later, someone makes a typo
hero["helth"] = 5  # Oops! Should be "hp"
# Python doesn't complain, but your game breaks mysteriously
```

**Problem 2: Inconsistent data structures**

```python
def create_mage(name):
    return {
        "name": name,
        "health": 8,  # Oops! Used "health" instead of "hp"
        "mana": 20
    }

mage = create_mage("Elena")
attack(hero, mage)  # Crash! "mana" has no "hp" key
```

**Problem 3: Functions don't know what they operate on**

```python
def attack(attacker, target):
    damage = attacker["strength"]  # What if attacker has no "strength"?
    target["hp"] -= damage         # What if target has no "hp"?
```

There's no way to guarantee that `attack` receives the right kind of dictionaries.

**Problem 4: Scattered logic**

Where is all the hero logic? In `create_hero`? In `attack`? In `is_alive`? It's everywhere!

```python
# Hero-related logic scattered across:
create_hero()      # Function 1
attack()           # Function 2
is_alive()         # Function 3
hero_level_up()    # Function 4
hero_heal()        # Function 5
# ... and so on
```

**Problem 5: No clear interface**

Looking at a dictionary, you can't tell what operations are valid:

```python
hero = create_hero("Olya")
# What can I do with a hero?
# I have to read the entire codebase to find out!
```

### Step 3: The OOP Solution

Now let's rebuild this using classes:

```python
# hero_oop_version.py
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.max_hp = 10
        self.strength = 2
    
    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.strength} damage!")
        target.take_damage(self.strength)
    
    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} HP: {self.hp}/{self.max_hp}")
    
    def is_alive(self):
        return self.hp > 0

class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
    
    def attack(self, target):
        damage = 1
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
    
    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} HP: {self.hp}/{self.max_hp}")
    
    def is_alive(self):
        return self.hp > 0

# Using the OOP system
hero = Hero("Olya")
enemy = Enemy("Slime", 5)

while hero.is_alive() and enemy.is_alive():
    hero.attack(enemy)
    if enemy.is_alive():
        enemy.attack(hero)

if hero.is_alive():
    print(f"{hero.name} wins!")
else:
    print(f"{enemy.name} wins!")
```

### Step 4: Benefits of the OOP Approach

**Benefit 1: Structure enforcement**

```python
hero = Hero("Olya")
# Python knows Hero objects have 'hp', 'name', 'strength'
# Your IDE can autocomplete these attributes
# Typos are caught immediately
```

**Benefit 2: Consistent interface**

Every `Hero` is guaranteed to have:
- `name`, `hp`, `max_hp`, `strength` attributes
- `attack()`, `take_damage()`, `is_alive()` methods

No surprises!

**Benefit 3: Clear organization**

All hero logic is in the `Hero` class. Want to know what heroes can do? Read the `Hero` class.

```python
class Hero:
    # Everything about heroes is RIGHT HERE
```

**Benefit 4: Self-documenting code**

```python
hero = Hero("Olya")
# I can see hero has: .attack(), .take_damage(), .is_alive()
# The class itself documents the interface
```

**Benefit 5: Easier to extend**

Want to add a heal method? Just add it to the `Hero` class:

```python
class Hero:
    # ... existing code ...
    
    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)
        print(f"{self.name} heals for {amount}! HP: {self.hp}/{self.max_hp}")
```

All heroes automatically get this new ability.

### Step 5: Side-by-Side Comparison

**Dictionary version:**
```python
hero = create_hero("Olya")
enemy = create_enemy("Slime", 5)
attack(hero, enemy)
if is_alive(hero):
    print("Hero survives")
```

**OOP version:**
```python
hero = Hero("Olya")
enemy = Enemy("Slime", 5)
hero.attack(enemy)
if hero.is_alive():
    print("Hero survives")
```

The OOP version is:
- More readable (`hero.attack(enemy)` reads like English)
- Self-contained (methods belong to objects)
- Safer (structure is enforced)
- Easier to extend and maintain

---

## Lesson Exercises

Complete these exercises to practice OOP concepts. Create your solutions in the `exercises/` directory.

### Exercise 1: Create an Enemy Class ⭐

**File:** `exercises/exercise_01_enemy.py`

Create an `Enemy` class with:
- `name` attribute (string)
- `hp` attribute (integer, default 5)
- A method `roar()` that prints "{name} roars menacingly!"

**Example usage:**
```python
slime = Enemy("Slime")
slime.roar()  # Slime roars menacingly!
print(slime.hp)  # 5
```

### Exercise 2: Add take_damage Method ⭐

**File:** `exercises/exercise_02_take_damage.py`

Extend the `Enemy` class from Exercise 1:
- Add a `take_damage(amount)` method that reduces HP by `amount`
- The method should print: "{name} takes {amount} damage! HP: {current_hp}"

**Example usage:**
```python
slime = Enemy("Slime")
slime.take_damage(2)  # Slime takes 2 damage! HP: 3
slime.take_damage(1)  # Slime takes 1 damage! HP: 2
```

### Exercise 3: Add is_alive Property ⭐⭐

**File:** `exercises/exercise_03_is_alive.py`

Extend your `Enemy` class:
- Add an `is_alive()` method that returns `True` if HP > 0, otherwise `False`

**Example usage:**
```python
slime = Enemy("Slime")
print(slime.is_alive())  # True

slime.take_damage(5)
print(slime.is_alive())  # False
```

### Exercise 4: Create a Hero Class ⭐⭐

**File:** `exercises/exercise_04_hero.py`

Create a `Hero` class with:
- `name` attribute (passed in `__init__`)
- `hp` attribute (default 10)
- `strength` attribute (default 2)
- A `greet()` method that prints "Hello, I am {name}!"

**Example usage:**
```python
hero = Hero("Olya")
hero.greet()  # Hello, I am Olya!
print(hero.hp)  # 10
print(hero.strength)  # 2
```

### Exercise 5: Hero Attacks Enemy ⭐⭐

**File:** `exercises/exercise_05_hero_attacks.py`

Create both `Hero` and `Enemy` classes:
- Hero has: `name`, `hp` (default 10), `strength` (default 2)
- Enemy has: `name`, `hp` (default 5)
- Hero has an `attack(enemy)` method that:
  - Reduces enemy HP by hero's strength
  - Prints: "{hero_name} attacks {enemy_name} for {strength} damage!"

**Example usage:**
```python
hero = Hero("Olya")
slime = Enemy("Slime")
hero.attack(slime)  # Olya attacks Slime for 2 damage!
print(slime.hp)  # 3
```

### Exercise 6: Simple Battle Round ⭐⭐⭐

**File:** `exercises/exercise_06_battle.py`

Extend your `Hero` and `Enemy` classes:
- Both should have `attack(target)` methods
- Both should have `take_damage(amount)` methods
- Both should have `is_alive()` methods
- Create a simple battle simulation where hero and enemy take turns attacking until one dies

**Example output:**
```
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
```

### Exercise 7: Add Healing ⭐⭐⭐

**File:** `exercises/exercise_07_healing.py`

Extend your `Hero` class:
- Add a `max_hp` attribute
- Add a `heal(amount)` method that:
  - Increases HP by `amount`
  - Doesn't let HP exceed `max_hp`
  - Prints: "{name} heals for {amount}! HP: {current_hp}/{max_hp}"

**Example usage:**
```python
hero = Hero("Olya")
hero.take_damage(5)  # HP: 5/10
hero.heal(3)         # Olya heals for 3! HP: 8/10
hero.heal(5)         # Olya heals for 5! HP: 10/10 (capped at max)
```

### Exercise 8: Resource System (Optional Challenge) ⭐⭐⭐⭐

**File:** `exercises/exercise_08_mana.py`

Create a `Mage` class with a mana system:
- Attributes: `name`, `hp` (default 8), `mana` (default 20), `max_mana` (default 20)
- `cast_spell(target, cost)` method:
  - Only works if mana >= cost
  - Reduces mana by cost
  - Deals 3 damage to target
  - Prints spell cast message
- `restore_mana(amount)` method (can't exceed max_mana)

**Example usage:**
```python
mage = Mage("Elena")
enemy = Enemy("Goblin", 10)

mage.cast_spell(enemy, 5)  # Costs 5 mana, deals 3 damage
mage.cast_spell(enemy, 5)
mage.cast_spell(enemy, 5)
mage.cast_spell(enemy, 5)
mage.cast_spell(enemy, 5)  # Should fail - not enough mana

mage.restore_mana(10)
mage.cast_spell(enemy, 5)  # Now it works
```

---

## Homework Assignment

Create a file `homework/rpg_classes.py` with the following OOP structures.

### Part 1: Item Class ⭐⭐

Create an `Item` class that represents items in an RPG:

**Requirements:**
- Attributes: `name` (string), `description` (string), `value` (int, gold value)
- Method: `describe()` - prints "{name}: {description} (Value: {value} gold)"

**Acceptance criteria:**
```python
sword = Item("Iron Sword", "A sturdy blade", 50)
sword.describe()  # Iron Sword: A sturdy blade (Value: 50 gold)
print(sword.value)  # 50
```

### Part 2: Inventory System ⭐⭐⭐

Create an `Inventory` class that manages items:

**Requirements:**
- Attribute: `items` (list of Item objects, initially empty)
- Method: `add_item(item)` - adds an item to inventory
- Method: `remove_item(item_name)` - removes first item with matching name
- Method: `list_items()` - prints all items in inventory
- Method: `total_value()` - returns sum of all item values

**Acceptance criteria:**
```python
inventory = Inventory()
inventory.add_item(Item("Potion", "Restores 5 HP", 10))
inventory.add_item(Item("Sword", "A sharp blade", 50))

inventory.list_items()
# Inventory:
# - Potion: Restores 5 HP (Value: 10 gold)
# - Sword: A sharp blade (Value: 50 gold)

print(inventory.total_value())  # 60

inventory.remove_item("Potion")
inventory.list_items()
# Inventory:
# - Sword: A sharp blade (Value: 50 gold)
```

### Part 3: Complete Hero Class ⭐⭐⭐

Create a full-featured `Hero` class:

**Requirements:**
- Attributes: `name`, `hp` (default 10), `max_hp` (default 10), `strength` (default 2), `inventory` (Inventory object)
- Method: `attack(target)` - deals strength damage to target
- Method: `take_damage(amount)` - reduces HP
- Method: `heal(amount)` - increases HP (capped at max_hp)
- Method: `is_alive()` - returns boolean
- Method: `pick_up_item(item)` - adds item to inventory
- Method: `show_status()` - prints hero stats and inventory

**Acceptance criteria:**
```python
hero = Hero("Olya")
hero.pick_up_item(Item("Potion", "Restores 5 HP", 10))
hero.pick_up_item(Item("Key", "Opens doors", 5))

hero.show_status()
# Hero: Olya
# HP: 10/10
# Strength: 2
# Inventory:
# - Potion: Restores 5 HP (Value: 10 gold)
# - Key: Opens doors (Value: 5 gold)
# Total value: 15 gold
```

### Submission Guidelines

1. Create a file `homework/rpg_classes.py`
2. Implement all three classes: `Item`, `Inventory`, `Hero`
3. Add a section at the bottom with test code demonstrating all functionality
4. Test your code thoroughly
5. Commit with message: "feat: complete OOP homework - RPG classes"
6. Create a pull request or submit according to instructor guidelines

### Bonus Challenge (Optional) ⭐⭐⭐⭐

Add a `Merchant` class:
- Attribute: `inventory` (Inventory object with items for sale)
- Method: `sell_to(hero, item_name)` - hero buys item if they have enough gold
- Method: `buy_from(hero, item_name)` - merchant buys item from hero

Implement a gold system for heroes to support buying/selling!

---

## Testing OOP Code

One of the benefits of OOP is that objects are easy to test! Let's see how to test our classes using pytest.

### Setting Up Tests

Create a file `tests/test_hero.py`:

```python
# tests/test_hero.py
import pytest
from oop_basics.examples.hero_oop_version import Hero, Enemy

def test_hero_creation():
    """Test that heroes are created with correct default values"""
    hero = Hero("Olya")
    assert hero.name == "Olya"
    assert hero.hp == 10
    assert hero.max_hp == 10
    assert hero.strength == 2

def test_hero_is_alive_when_healthy():
    """Test that hero is alive when HP > 0"""
    hero = Hero("Olya")
    assert hero.is_alive() == True

def test_hero_is_dead_when_hp_zero():
    """Test that hero is dead when HP <= 0"""
    hero = Hero("Olya")
    hero.hp = 0
    assert hero.is_alive() == False

def test_hero_takes_damage():
    """Test that hero HP decreases when taking damage"""
    hero = Hero("Olya")
    hero.take_damage(3)
    assert hero.hp == 7

def test_hero_attack_reduces_enemy_hp():
    """Test that hero attack reduces enemy HP by hero's strength"""
    hero = Hero("Olya")
    enemy = Enemy("Slime", 5)
    
    hero.attack(enemy)
    
    assert enemy.hp == 3  # 5 - 2 (hero strength)

def test_multiple_attacks():
    """Test a sequence of attacks"""
    hero = Hero("Olya")
    enemy = Enemy("Slime", 5)
    
    hero.attack(enemy)  # HP: 3
    hero.attack(enemy)  # HP: 1
    hero.attack(enemy)  # HP: -1
    
    assert enemy.is_alive() == False
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest -v tests/

# Run a specific test file
pytest tests/test_hero.py

# Run a specific test
pytest tests/test_hero.py::test_hero_attack_reduces_enemy_hp
```

### Why Testing OOP is Great

**1. Objects are isolated**

Each test creates fresh objects, so tests don't interfere with each other:

```python
def test_one():
    hero = Hero("Olya")
    hero.hp = 5
    # This hero only exists in this test

def test_two():
    hero = Hero("Ivan")
    # Fresh hero, unaffected by test_one
```

**2. Easy to set up test scenarios**

```python
def test_low_hp_hero():
    hero = Hero("Olya")
    hero.hp = 1  # Set up specific scenario
    # Now test behavior
```

**3. Clear expectations**

```python
def test_hero_attack():
    hero = Hero("Olya")
    enemy = Enemy("Slime", 5)
    
    hero.attack(enemy)
    
    # Clear expectation: enemy HP should be reduced
    assert enemy.hp == 3
```

### Exercise: Write Your Own Tests

Create `tests/test_exercises.py` and write tests for your exercise solutions:

1. Test that `Enemy` is created with correct attributes
2. Test that `take_damage` reduces HP correctly
3. Test that `is_alive` returns correct boolean
4. Test a complete battle scenario

---

## Summary

Congratulations! You've learned the fundamentals of Object-Oriented Programming in Python.

**Key takeaways:**

✅ **Classes** are blueprints for creating objects  
✅ **Objects** are instances of classes with their own state  
✅ **Attributes** store object data  
✅ **Methods** define object behavior  
✅ **Encapsulation** bundles data and behavior together  
✅ **OOP** makes code more organized, maintainable, and natural to reason about

**Next steps:**

- Complete all exercises to solidify your understanding
- Work on the homework assignment
- Practice writing tests for your classes
- Start thinking about your own projects in terms of objects

**Looking ahead:**

In future lessons, you'll learn:
- Inheritance (creating classes based on other classes)
- Polymorphism (objects behaving differently based on their type)
- Advanced OOP patterns and best practices
- Integrating OOP with real-world projects

Keep practicing, and remember: OOP is a tool to help you organize code. Use it when it makes your code clearer, not just because you can!

Happy coding! 🚀
