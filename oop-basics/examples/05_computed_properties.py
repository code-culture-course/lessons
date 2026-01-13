"""
Example 5: Computed Properties

This example shows:
- Methods that return values
- Computed properties (methods that calculate values on the fly)
- Using methods for game logic (alive checks, percentages, status)
"""


class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.max_hp = 10
    
    def is_alive(self):
        """Return True if hero is alive, False otherwise"""
        return self.hp > 0
    
    def hp_percentage(self):
        """Calculate HP as a percentage of max HP"""
        return (self.hp / self.max_hp) * 100
    
    def status(self):
        """Return a status description based on current HP"""
        if self.hp == self.max_hp:
            return "healthy"
        elif self.hp > self.max_hp / 2:
            return "wounded"
        elif self.hp > 0:
            return "critical"
        else:
            return "dead"
    
    def show_status(self):
        """Display full status information"""
        print(f"{self.name} - {self.status()}")
        print(f"  HP: {self.hp}/{self.max_hp} ({self.hp_percentage():.1f}%)")
        print(f"  Alive: {self.is_alive()}")


if __name__ == "__main__":
    hero = Hero("Olya")
    
    print("=== Full Health ===")
    hero.show_status()
    # Olya - healthy
    #   HP: 10/10 (100.0%)
    #   Alive: True
    
    print("\n=== After Taking Damage ===")
    hero.hp = 7
    hero.show_status()
    # Olya - wounded
    #   HP: 7/10 (70.0%)
    #   Alive: True
    
    print("\n=== Critical Condition ===")
    hero.hp = 3
    hero.show_status()
    # Olya - critical
    #   HP: 3/10 (30.0%)
    #   Alive: True
    
    print("\n=== Defeated ===")
    hero.hp = 0
    hero.show_status()
    # Olya - dead
    #   HP: 0/10 (0.0%)
    #   Alive: False
