class Item:

    def __init__(self, name, category, is_equipable=False, quantity=1, encumbrance_modifier=0,encumbrance_ranged_modifier=0, attack_modifier=0, armor_modifier=0, health_modifier=0, health_max_modifier=0, magic_modifier=0, agility_modifier=0, abilities_modifier=0):

        #item lists
        #weapons
        onehanded_weapons = ["sword","axe","hammer","staff"]
        twohanded_weapons = ["spear", "broadsword", "battle axe", "polearm"]
        light_weapons = ["short sword", "dagger"]

        melee_weapons = onehanded_weapons + twohanded_weapons + light_weapons
        ranged_weapons = ["sling", "bow", "crossbow"]

        #armors
        light_armors = ["leather armor", "chain mail"]
        heavy_armors = ["plate armor"]

        armors = light_armors + heavy_armors

        #utilities
        #[TO-DO]create utilities


        #create standard item
        #if only 1 argument, and argument is string
        if len(args) == 1 and isinstance (args[0], str):
            name = args[0]
            self.name = name

            #melee weapon
            if name in melee_weapons:
                self.category = "melee_weapon"
                self.is_equipable = True

                if name in onehanded_weapons+light_weapons:
                    self.encumbrance_modifier = 1
                elif name in heavy_weapons:
                    self.encumbrance_modifier = 2

                if name in light_weapons:
                    self.agility_modifier = 1
                    #[TO-DO] add +1 armor for enemies

                if name in heavy_weapons:
                    self.agility_modifier = -1
                    #[TO-DO] add -1 armor for enemies

            #ranged weapon
            elif name in ranged_weapons:
                self.category = "ranged_weapon"
                self.is_equipable = True
                self.encumbrance_ranged_modifier = 2 
                
                if name == "sling":
                    self.attack_modifier = 1
                elif name == "bow":
                    self.attack_modifier = 2
                elif name == "crossbow":
                    self.attack_modifier = 3

            #armor
            elif name in armors:
                self.categoy = "armor"
                self.is_equipable = True
                if name in light_armors:
                    self.armor_modifier = "1"
                elif name in heavy_armors:
                    self.armor_modifier = "2"
                    #[TO-DO] add no magic


            #utility
            else:
                self.category = utility


        #new non standard item
        self.name = name
        self.category = category
            #armor, melee_weapon, ranged_weapon, utility
        self.is_equipable = is_equipable
        self.encumbrance_modifier = encumbrance_modifier
        self.encumbrance_ranged_modifier = encumbrance_ranged_modifier
        self.quantity = quantity
        self.attack_modifier = attack_modifier
        self.armor_modifier = armor_modifier
        self.health_modifier = health_modifier
        self.health_max_modifier = health_max_modifier
        self.magic_modifier = magic_modifier
        self.agility_modifier = agility_modifier
        self.abilities_modifier = abilities_modifier

