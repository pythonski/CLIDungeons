from random import randint

class Character:
    
    def __init__(self, isPlayer, name, role, attack, armor, health, magic, agility, inventory, abilities):
        self.isPlayer = isPlayer
        self.name = name
        self.role = role
        self.attack = attack
        self.health = health
        self.magic = magic
        self.agility = agility
        self.inventory = inventory
        self.abilities = abilities
        
    def throw():
        result = []
        for die in range(self.attack):
            result.append(randint(1,6))
        
        return result
