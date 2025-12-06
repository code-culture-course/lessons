# Testing Guide for OOP Code

This directory contains test examples for the OOP lessons using pytest.

## Why Test OOP Code?

Testing object-oriented code is especially valuable because:

1. **Objects are isolated** - Each test creates fresh objects
2. **State is encapsulated** - Tests can verify internal state changes
3. **Interactions are clear** - Easy to test how objects work together
4. **Regression protection** - Catch bugs when you modify classes

## Running Tests

### Install pytest (if needed)

```bash
pip install pytest
```

### Run all tests

```bash
pytest tests/
```

### Run with verbose output

```bash
pytest -v tests/
```

### Run a specific test file

```bash
pytest tests/test_hero.py
```

### Run a specific test class

```bash
pytest tests/test_hero.py::TestHeroAttack
```

### Run a specific test method

```bash
pytest tests/test_hero.py::TestHeroAttack::test_hero_attack_reduces_enemy_hp
```

## Test Structure

Our test file (`test_hero.py`) demonstrates several testing patterns:

### 1. Organizing Tests into Classes

```python
class TestHeroCreation:
    """Tests for hero object creation"""
    
    def test_hero_has_correct_default_values(self):
        # Test code here
```

Grouping related tests into classes makes them easier to understand and run selectively.

### 2. Testing Object Creation

```python
def test_hero_has_correct_default_values(self):
    hero = Hero("Olya")
    
    assert hero.name == "Olya"
    assert hero.hp == 10
```

Verify objects are initialized correctly.

### 3. Testing Methods

```python
def test_hero_takes_damage(self):
    hero = Hero("Olya")
    hero.take_damage(3)
    assert hero.hp == 7
```

Call methods and verify they produce expected results.

### 4. Testing Object Interactions

```python
def test_hero_attack_reduces_enemy_hp(self):
    hero = Hero("Olya")
    enemy = Enemy("Slime", 5)
    
    hero.attack(enemy)
    
    assert enemy.hp == 3
```

Test how objects affect each other.

### 5. Testing Edge Cases

```python
def test_zero_hp_enemy_is_not_alive(self):
    enemy = Enemy("Slime", 5)
    enemy.hp = 0
    
    assert enemy.is_alive() == False
```

Test boundary conditions and special cases.

## Writing Your Own Tests

### Test Naming Convention

- Test files: `test_*.py`
- Test functions: `def test_*():`
- Test classes: `class Test*:`

### Good Test Structure (AAA Pattern)

```python
def test_something():
    # Arrange - Set up test data
    hero = Hero("Olya")
    
    # Act - Perform the action
    hero.take_damage(5)
    
    # Assert - Check the result
    assert hero.hp == 5
```

### What to Test

✅ **Do test:**
- Object creation (correct initialization)
- Method behavior (correct outputs/state changes)
- Edge cases (zero, negative, boundary values)
- Object interactions
- Error handling

❌ **Don't test:**
- Python built-in functionality
- Third-party library internals
- Trivial getters/setters (unless they have logic)

## Exercise: Write Tests for Your Exercises

Create `test_exercises.py` and write tests for your exercise solutions:

```python
# test_exercises.py
from exercises.exercise_01_enemy import Enemy

def test_enemy_creation():
    enemy = Enemy("Slime")
    assert enemy.name == "Slime"
    assert enemy.hp == 5

def test_enemy_roar():
    enemy = Enemy("Goblin")
    # How would you test that roar() prints correctly?
    # (Hint: look up pytest capsys fixture)
```

## Common Pytest Features

### Assertions

```python
assert value == expected
assert hero.is_alive() == True
assert enemy.hp > 0
```

### Testing for Exceptions

```python
import pytest

def test_invalid_input():
    with pytest.raises(ValueError):
        hero = Hero("")  # Empty name should raise error
```

### Fixtures (Reusable Test Data)

```python
import pytest

@pytest.fixture
def hero():
    return Hero("Olya")

def test_hero_attack(hero):  # pytest injects the fixture
    enemy = Enemy("Slime", 5)
    hero.attack(enemy)
    assert enemy.hp == 3
```

### Parametrized Tests

```python
import pytest

@pytest.mark.parametrize("damage,expected_hp", [
    (1, 9),
    (5, 5),
    (10, 0),
])
def test_hero_takes_various_damage(damage, expected_hp):
    hero = Hero("Olya")
    hero.take_damage(damage)
    assert hero.hp == expected_hp
```

## Tips for Testing OOP

1. **Test one thing at a time** - Each test should verify one behavior
2. **Use descriptive names** - `test_hero_attack_reduces_enemy_hp` is better than `test_attack`
3. **Keep tests independent** - Each test should work on its own
4. **Test behavior, not implementation** - Test what the method does, not how it does it
5. **Write tests as you code** - Don't wait until the end

## Further Reading

- [Pytest documentation](https://docs.pytest.org/)
- [Python testing guide](https://realpython.com/pytest-python-testing/)
- [Test-Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development)

---

Happy testing! 🧪
