from random import randint

class Character:
    
    def __init__(self, isPlayer=False, isNew=None, name=None, role=None, attack=None, armor=None, health=None, health_max=None, encumbrance=None, magic=None, agility=None, money=None, equipment=None, inventory=None, abilities=None):
        #barbarian
        if role == 'b' and isNew == True:
            self.isPlayer = True
            self.name = name
            self.name = role
            self.attack = 3
            self.armor = 3
            self.health = 6
            self.health_max = 6
            self.encumbrance = 1
            self.magic = 0
            self.agility = 2
            self.money = 0
            self.equipment = ["ascia"]
            self.inventory = {} 
            self.abilities = []

        #dwarf
        if role == 'd' and isNew == True:
            self.isPlayer = True
            self.name = name
            self.name = role
            self.attack = 2
            self.armor = 5
            self.health = 5
            self.health_max = 5
            self.encumbrance = 1
            self.magic = 0
            self.agility = 1
            self.money = 0
            self.equipment = ["ascia, "armatura pesante"]
            self.inventory = {} 
            self.abilities = []


        #load character from file
        if isNew == False:
            self.isPlayer = isPlayer
            self.isNew = isNew
            self.name = name
            self.role = role
            self.attack = attack
            self.armor = armor
            self.health = health
            self.health_max = health_max
            self.encumbrance = encumbrance
            self.magic = magic
            self.agility = agility
            self.money = money
            self.equipment = equipment
            self.inventory = inventory
            self.abilities = abilities
        
    def throw (self):
        result = []
        for die in range (self.attack):
            result.append (randint (1,6))
        
        return result

    #equip item and apply modifier
#    def equip (self, item):
# to do
# check encumbrance
# check number of items (double of health)
# other checks

    #unequip item and de-apply modifiers
