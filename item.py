class Item:

    def __init__(self, name, category, quantity=1, encumbrance_modifier=0, attack_modifier=0, armor_modifier=0, health_modifier=0, health_max_modifier=0, magic_modifier=0, agility_modifier=0, abilities_modifier=0):

        self.name = name
        self.category = name
        self.quantity = quantity
        self.encumbrance = encumbrance
        self.attack_modifier = attack_modifier
        self.armor_modifier = armor_modifier
        self.health_modifier = health_modifier
        self.health_max_modifier = health_max_modifier
        self.encumbrance_modifier = encumbrance_modifier
        self.magic_modifier = magic_modifier
        self.agility_modifier = agility_modifier
        self.abilities_modifier = abilities_modifier

