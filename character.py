from random import randint

class Character:
    
    def __init__(self, isPlayer, name, role, attack, armor, health, magic, agility, money, inventory, abilities):
        self.isPlayer = isPlayer
        self.name = name
        self.role = role
        self.attack = attack
        self.armor = armor
        self.health = health
        self.magic = magic
        self.agility = agility
        self.money = money
        self.inventory = inventory
        self.abilities = abilities
        
    def throw(self):
        result = []
        for die in range(self.attack):
            result.append(randint(1,6))
        
        return result
