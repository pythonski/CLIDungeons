def determine_first(player, enemy):
    
    while(True):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        
        if die1 > die2 : return [player, enemy]
        elif die1 < die2 : return [enemy, player]
        
def fight(player, enemy):
    
    # decide who attacks first
    
    if player.agility < enemy.agility:
        first = enemy
        second = player

    elif player.agility > enemy.agility:
        first = player
        second = enemy
        
    else: 
        first, second = determine_first(player, enemy)
        
    # fight to the death!
        
    while(first.health > 0 and second.health > 0):
        
        print(f"It's {first.name}'s turn!")
        
        result = first.throw()
        print(f"{first.name} has thrown {result}.")
        
        damage = 0 # keep track of damage
        
        for value in result:
            if value >= second.armor: 
                second.health -= 1
                damage += 1

        print(f"{second.name} has lost {damage} health points!")

        # swap attacker and defender
        first, second = second, first
    
    # if the player is dead, the game ends
    
    if (second.health <= 0 and second.isPlayer) or (first.health <= 0 and first.isPlayer): 
        print(f"You die!")
        return -1

    # if not determine health points left
    else:
        
        if first.isPlayer:
            print(f"You win! You have {first.health} health points left")
            player.health = first.health
            return 0

        else:
            print(f"You win! You have {second.health} health points left")
            player.health = second.health
            return 0 
