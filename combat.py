import random
randomchance = [1,2,3,4,5,6,7,8,9,10]
encounterchance = random.choice(randomchance)

if encounterchance == 10:
    slime = [
        "  ____  ",
        " / | |\\ ",
        "|   _  | ",
        "\\______/ ",
        "You are being attacked!"
        ]
    for line in slime:
            print (line)
            current_enemy = slime
            incombat = True

    
if encounterchance == 5:
    goblin_not_those_nuts = [
        " \\[:(]/",
        "  / \\  "
        "You are being attacked!"
        ]
    for line in goblin_not_those_nuts:
        print (line)
        current_enemy = goblin_not_those_nuts
        incombat = True
                
else:
    print ("You don't find enemies.")

    combatoptions = [
        "1. Attack!",
        "2. Items",
        "3. Run"
        ]

    combatoptions = [
        "1. Attack!",
        "2. Items",
        "3. Run"
        ]

if incombat == True:
    while incombat:
        for line in combatoptions:
            print(line)
            combatinput = input("What would you like to do? ")

        if combatinput == "1":
            if current_enemy:
                current_enemy.hp -= player_strength
                #Add a way to make the combat exciting. Maybe make the player click at the right time to crit!
                print(f"You attack the {current_enemy.name} for {player_strength} damage!")

            if current_enemy.hp <= 0:
                print(f"You defeated the {current_enemy.name}!")
                player_money += current_enemy.reward
                print(f"You received 50 gold! You now have {player_money} gold.")
                incombat = False

        elif combatinput == "2":
            ininventory = True
            for line in player_inventory:
                print(line)
                inventoryinput = input("What item would you like to use?").lower
                if inventoryinput == "healing potion" and "healing potion" in player_inventory:
                    player_health += 20
                    print(f"You used a healing potion! Your HP is now {player_health}.")
                    player_inventory.remove("healing potion")
                elif inventoryinput == "q":
                    ininventory = False


        elif combatinput == "3":
            print(f"You ran from the {current_enemy.name} like the baby you are.")
            incombat = False 
            current_enemy = None 

    if not incombat:
        print("Combat is over.")

def take_damage(character, damage):
    character.hp -= damage
    print(f"{character.name} takes {damage} damage! Remaining HP: {character.hp}")

if current_enemy:
    take_damage(player_health, current_enemy.attack)