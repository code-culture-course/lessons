"""
Test examples for OOP classes

These tests demonstrate how to test object-oriented code using pytest.
They show good practices for testing classes, methods, and object interactions.

To run these tests:
    pytest tests/test_hero.py
    
To run with verbose output:
    pytest -v tests/test_hero.py
"""

import sys
import os

# Add parent directory to path so we can import examples
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from examples.hero_oop_version import Hero, Enemy


class TestHeroCreation:
    """Tests for hero object creation"""
    
    def test_hero_has_correct_default_values(self):
        """Hero should be created with expected default attributes"""
        hero = Hero("Olya")
        
        assert hero.name == "Olya"
        assert hero.hp == 10
        assert hero.max_hp == 10
        assert hero.strength == 2
    
    def test_multiple_heroes_are_independent(self):
        """Multiple heroes should have independent state"""
        hero1 = Hero("Olya")
        hero2 = Hero("Ivan")
        
        hero1.hp = 5
        
        assert hero1.hp == 5
        assert hero2.hp == 10  # hero2 is unaffected


class TestHeroAliveStatus:
    """Tests for hero alive/dead status"""
    
    def test_hero_is_alive_with_positive_hp(self):
        """Hero with HP > 0 should be alive"""
        hero = Hero("Olya")
        assert hero.is_alive() == True
    
    def test_hero_is_dead_with_zero_hp(self):
        """Hero with HP = 0 should be dead"""
        hero = Hero("Olya")
        hero.hp = 0
        assert hero.is_alive() == False
    
    def test_hero_is_dead_with_negative_hp(self):
        """Hero with HP < 0 should be dead"""
        hero = Hero("Olya")
        hero.hp = -5
        assert hero.is_alive() == False


class TestHeroDamage:
    """Tests for taking damage"""
    
    def test_hero_takes_damage(self):
        """Taking damage should reduce HP"""
        hero = Hero("Olya")
        hero.take_damage(3)
        assert hero.hp == 7
    
    def test_hero_takes_multiple_damage(self):
        """Multiple damage events should accumulate"""
        hero = Hero("Olya")
        hero.take_damage(2)
        hero.take_damage(3)
        hero.take_damage(1)
        assert hero.hp == 4
    
    def test_hero_can_take_fatal_damage(self):
        """Hero can take enough damage to die"""
        hero = Hero("Olya")
        hero.take_damage(15)
        assert hero.hp < 0
        assert hero.is_alive() == False


class TestHeroAttack:
    """Tests for hero attacking enemies"""
    
    def test_hero_attack_reduces_enemy_hp(self):
        """Hero attack should reduce enemy HP by hero's strength"""
        hero = Hero("Olya")
        enemy = Enemy("Slime", 5)
        
        hero.attack(enemy)
        
        assert enemy.hp == 3  # 5 - 2 (hero strength)
    
    def test_multiple_attacks(self):
        """Multiple attacks should accumulate damage"""
        hero = Hero("Olya")
        enemy = Enemy("Slime", 10)
        
        hero.attack(enemy)  # HP: 8
        hero.attack(enemy)  # HP: 6
        hero.attack(enemy)  # HP: 4
        
        assert enemy.hp == 4
    
    def test_hero_can_defeat_enemy(self):
        """Hero should be able to defeat enemy through attacks"""
        hero = Hero("Olya")
        enemy = Enemy("Slime", 5)
        
        hero.attack(enemy)  # HP: 3
        hero.attack(enemy)  # HP: 1
        hero.attack(enemy)  # HP: -1
        
        assert enemy.is_alive() == False


class TestEnemyCreation:
    """Tests for enemy object creation"""
    
    def test_enemy_created_with_correct_attributes(self):
        """Enemy should be created with specified name and HP"""
        enemy = Enemy("Goblin", 8)
        
        assert enemy.name == "Goblin"
        assert enemy.hp == 8
        assert enemy.max_hp == 8
    
    def test_enemy_with_different_hp(self):
        """Different enemies can have different HP values"""
        weak_enemy = Enemy("Slime", 3)
        strong_enemy = Enemy("Dragon", 20)
        
        assert weak_enemy.hp == 3
        assert strong_enemy.hp == 20


class TestCombatScenarios:
    """Tests for complete combat scenarios"""
    
    def test_simple_battle_hero_wins(self):
        """Hero with advantage should win battle"""
        hero = Hero("Olya")
        hero.strength = 3  # Stronger than normal
        enemy = Enemy("Slime", 5)
        
        while hero.is_alive() and enemy.is_alive():
            hero.attack(enemy)
            if enemy.is_alive():
                enemy.attack(hero)
        
        assert hero.is_alive() == True
        assert enemy.is_alive() == False
    
    def test_battle_with_weak_hero(self):
        """Weak hero should lose to strong enemy"""
        hero = Hero("Olya")
        hero.strength = 1
        hero.hp = 5
        enemy = Enemy("Dragon", 20)
        
        # Hero attacks a few times
        for _ in range(3):
            hero.attack(enemy)
        
        # Enemy should still be alive
        assert enemy.is_alive() == True
        # Enemy hasn't attacked back yet in this test
        assert hero.is_alive() == True


class TestEdgeCases:
    """Tests for edge cases and boundary conditions"""
    
    def test_attack_already_dead_enemy(self):
        """Attacking dead enemy should still work (HP goes negative)"""
        hero = Hero("Olya")
        enemy = Enemy("Slime", 1)
        
        hero.attack(enemy)  # HP: -1
        hero.attack(enemy)  # HP: -3
        
        assert enemy.hp == -3
        assert enemy.is_alive() == False
    
    def test_zero_hp_enemy_is_not_alive(self):
        """Enemy with exactly 0 HP should be dead"""
        enemy = Enemy("Slime", 5)
        enemy.hp = 0
        
        assert enemy.is_alive() == False
    
    def test_one_hp_enemy_is_alive(self):
        """Enemy with 1 HP should still be alive"""
        enemy = Enemy("Slime", 5)
        enemy.hp = 1
        
        assert enemy.is_alive() == True


# Example of how to run specific tests
if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
