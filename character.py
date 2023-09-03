from random import randint

class Character:
    
    def __init__(self, isPlayer=False, isNew=None, name=None, role=None, attack=None, armor=None, health=None, health_max=None, encumbrance=None, encumbrance_ranged=None, magic=None, agility=None, money=None, equipment=None, inventory=None, abilities=None):
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
            self.encumbrance_ranged = 0
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
            self.encumbrance_ranged = 0
            self.magic = 0
            self.agility = 1
            self.money = 0
            self.equipment = ["ascia", "armatura pesante"]
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
            self.encumbrance_ranged = encumbrance_ranged
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


    #equip item from inventory
    def equip(self, item):
        if item in self.inventory and item.is_equipable: 

            #armor
            if (item.category == "armor"):
                current_armor = [item for item in self.equipment if item.category == "armor"]
                #if currently armor, remove
                if (current_armor):
                    self.unequip (current_armor)

            #weapon or utility
            if (self.encumbrance + item.encumbrance_modifier > 2) or (self.encumbrance_ranged + item.encumbrance_ranged_modifier > 2):
                print(f"Cannot equip {item.name}: exceeding maximum encumbrance!)\n")
                return
            
            #equip item
            else:
                #move to equipment
                self.inventory.remove (item)
                self.equipment.append(item)

                #apply encumbrance
                self.encumbrance += item.encumbrance_modifier
                self.encumbrance_ranged += item.ecumbrance_ranged_modifier

                #apply modifiers
                self.attack += item.attack_modifier
                self.armor += item.armor_modifier
                self.health += item.health_modifier
                self.health_max += item.health_max_modifier
                self.magic += item.magic_modifier
                self.agility += item.agility_modifier
                self.abilities.append(item.abilities_modifier)

        else:
            print(f"Item {item.name} cannot be equipped.\n")
            return   


    #Unequip item from equipment and put it in inventory
    def unequip(self, item):

        if item in self.equipment:

            #move to inventory
            self.equipment.remove (item)
            self.inventory.append (item)

            #remove encumbrance
            self.encumbrance -= item.encumbrance_modifier
            self.encumbrance_ranged -= item.ecumbrance_ranged_modifier

            #remove modifiers
            self.attack -= item.attack_modifier
            self.armor -= item.armor_modifier
            self.health -= item.health_modifier
            self.health_max -= item.health_max_modifier
            self.magic -= item.magic_modifier
            self.agility -= item.agility_modifier
            self.abilities.remove(item.abilities_modifier) 

        else:
            print(f"You do not have {item.name} equipped.\n")

        #TO-DO: pickup and drop object
