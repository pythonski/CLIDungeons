from random import randint

def user_choose(message, choices):

    choice = None
    while not choice in choices:
        choice = input(message).lower()
        if choice not in choices:
            print("\nChoice is invalid. Try again.\n") 
        
    return choice

class Character:
    # to add: proper docs
    
    def __init__(self, is_player=False, is_new=None, name=None, role=None, attack=None, armor=None, health=None, health_max=None, encumbrance=None, encumbrance_ranged=None, inventory_capacity=None, magic=None, agility=None, money=None, equipment=None, inventory=None, abilities=None):
        #barbarian
        if role == 'b' and is_new == True:
            self.is_player = True
            self.name = name
            self.role = "barbarian"
            self.attack = 3
            self.armor = 3
            self.health = 6
            self.health_max = 6
            self.encumbrance = 1
            self.encumbrance_ranged = 0
            self.inventory_capacity = 12
            self.magic = 0
            self.agility = 2
            self.money = 0
            self.equipment = [] # WATCH THIS: THERE SHOULD BE AN AXE OBJECT HERE
            self.inventory = [] # list instead of dictionary?
            self.abilities = []

        #dwarf
        if role == 'd' and is_new == True:
            self.is_player = True
            self.name = name
            self.role = "dwarf"
            self.attack = 2
            self.armor = 5
            self.health = 5
            self.health_max = 5
            self.encumbrance = 1
            self.encumbrance_ranged = 0
            self.inventory_capacity = 10
            self.magic = 0
            self.agility = 1
            self.money = 0
            self.equipment = [] # THERE SHOULD BE AXE AND HEAVY ARMOR OBJECTS HERE
            self.inventory = [] # list instead of dictionary?
            self.abilities = []


        #load character from file
        if is_new == False:
            self.is_player = is_player
            self.is_new = is_new
            self.name = name
            self.role = role
            self.attack = attack
            self.armor = armor
            self.health = health
            self.health_max = health_max
            self.encumbrance = encumbrance
            self.encumbrance_ranged = encumbrance_ranged
            self.inventory_capacity = inventory_capacity
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
                #if currently wearing armor, remove
                if (current_armor):
                    self.unequip(*current_armor)

            #weapon or utility
            if (self.encumbrance + item.encumbrance_modifier > 2) or (self.encumbrance_ranged + item.encumbrance_ranged_modifier > 2):
                print(f"Cannot equip {item.name}: exceeding maximum encumbrance!)\n")
                return
            
            #equip item
            else:
                #move to equipment
                if item.quantity == 1:
                    self.inventory.remove(item)
                else:
                    item.quantity -= 1

                self.equipment.append(item)

                #apply encumbrance
                self.encumbrance += item.encumbrance_modifier
                self.encumbrance_ranged += item.encumbrance_ranged_modifier

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
            self.equipment.remove(item)
            if item in self.inventory:
                self.inventory[self.inventory.index(item)].quantity += 1
            else:
                self.inventory.append(item)

            #remove encumbrance
            self.encumbrance -= item.encumbrance_modifier
            self.encumbrance_ranged -= item.encumbrance_ranged_modifier

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

    def pickup(self, item):

        #check if not exceeding maximum inventory capacity
        current_capacity = sum([item.quantity for item in self.inventory])
        if current_capacity == self.inventory_capacity:
            print(f"\n\
> Item {item.name} cannot be picked up. Inventory is full.\n\
    [D]iscard      [M]ake room\n")
            choice = '' 

            while (choice != 'd' and choice != 'm'):
                choice = input().lower()
                if choice == 'm':
                    self.manage_inventory()
                    self.pickup(item)

        else:
            if item in self.inventory:
                self.inventory[self.inventory.index(item)].quantity += 1
            else:
                self.inventory.append(item)

    def drop(self, item):
        if item.quantity > 1:
            item.quantity -= 1
        else:
            self.inventory.remove(item)

    def manage_inventory(self):

        print("Your inventory is:\n")
        
        item_names = [item.name for item in self.inventory]
        equipped_items_names = [item.name for item in self.equipment]
        item_quantities = [item.quantity for item in self.inventory] 
        
        stuff = dict(zip(item_names, item_quantities))
        print(stuff)
        
        print(f"\n Your current equipment is:\n {equipped_items_names}")
        
        choice = user_choose("\n What do you want to do? \n\n\
>   [D]iscard item  [H]eal using item\n\
    [E]quip item    [U]nequip item\n\
    [S]ee stats     [C]ancel\n", ["d", "u", "s", "e", "h", "c"])
      
        if choice == "c":
            return
            
        if choice == "d":
            stop = False
            item_names_to_discard = []
            
            while(not stop):
                selected_item_name = user_choose("\nChoose item to discard (or [C]ancel): ", item_names + ["c"])
                
                if selected_item_name == "c": return
                
                selected_item = [item for item in self.inventory if item.name == selected_item_name][0]
             
                # dialog for items with quantity > 1
                if selected_item.quantity > 1:
                    choice = user_choose(f"\n\
> How many? (1 - {selected_item.quantity})\n", [str(n) for n in range(1, selected_item.quantity+1)])
                    item_names_to_discard.append([selected_item_name]*int(choice))
                else:
                    item_names_to_discard.append(selected_item_name)
                
                choice = user_choose("\n[S]top or [C]ontinue discarding? ", ["s", "c"])
                if choice == "s" : stop = True
            
            # maybe add confirmation
            
            items_to_discard = [item for item in self.inventory if item.name in item_names_to_discard]
            for item in items_to_discard: 
                self.drop(item)
                
        if choice == "s":
            item_to_examine_name = user_choose("\nChoose item to examine (or [C]ancel): ", item_names + equipped_items_names + ["c"])
            if item_to_examine_name == "c": return
            # maybe add description of objects as attribute in Item

            item_to_examine = [item for item in self.inventory + self.equipment if item.name == item_to_examine_name][0]

            print(vars(item_to_examine))
            
        if choice == "e":
            item_to_equip_name = user_choose("\nChoose item to equip (or [C]ancel): ", item_names + ["c"])
            if item_to_equip_name == "c": return

            item_to_equip = [item for item in self.inventory if item.name == item_to_equip_name][0]
            
            self.equip(item_to_equip) # assume all checks are done in the equip function
            
        if choice == "u":
            item_to_unequip_name = user_choose("\nChoose item to unequip (or [C]ancel): ", equipped_items_names + ["c"])
            if item_to_unequip_name == "c": return
            
            item_to_unequip = [item for item in self.equipment if item.name == item_to_unequip_name[0]]

            self.unequip(item_to_unequip)
            
        if choice == "h":
            
            usable_items = ["health potion", "bandage"]
        
            item_name = user_choose("\nChoose item to use (or [C]ancel): ", [item.name for item in self.inventory if item.name in usable_items] + ["c"])
                
            if item_name == "c": return
                
            item_to_use = [item for item in self.inventory if item.name == item_name][0]
                
            # apply effect
            if self.health + item_to_use.health_modifier > self.health_max:
                self.health = self.health_max
            else:
                self.health += item_to_use.health_modifier 
            # discard
            self.drop(item_to_use)  
