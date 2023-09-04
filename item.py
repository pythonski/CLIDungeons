class Item:

    def __init__(self, name, category, is_equipable=False, quantity=1, encumbrance_modifier=0,encumbrance_ranged_modifier=0, attack_modifier=0, armor_modifier=0, health_modifier=0, health_max_modifier=0, magic_modifier=0, agility_modifier=0, abilities_modifier=0):

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

