class Character:
    def __init__(self, base_stat):
        self.base_stat = base_stat
        self.life = base_stat
        self.attack = base_stat
        self.defense = base_stat
        self.range = base_stat

class Knight(Character):
    def __init__(self, base_stat):
        super().__init__(base_stat)
        self.life = base_stat * 2
        self.defense = base_stat * 2

class Warrior(Character):
    def __init__(self, base_stat):
        super().__init__(base_stat)
        self.attack = base_stat * 2
        self.range = base_stat * 2

class Archer(Character):
    def __init__(self, base_stat):
        super().__init__(base_stat)
        self.defense = base_stat / 2
        self.range = base_stat * 2

# Create instances of each character class
knight = Knight(2)
warrior = Warrior(2)
archer = Archer(2)

# Display the properties of each character
print("Knight:")
print("Life:", knight.life)
print("Attack:", knight.attack)
print("Defense:", knight.defense)
print("Range:", knight.range)
print()

print("Warrior:")
print("Life:", warrior.life)
print("Attack:", warrior.attack)
print("Defense:", warrior.defense)
print("Range:", warrior.range)
print()

print("Archer:")
print("Life:", archer.life)
print("Attack:", archer.attack)
print("Defense:", archer.defense)
print("Range:", archer.range)