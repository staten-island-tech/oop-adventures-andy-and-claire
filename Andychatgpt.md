# ChatGPT Coding Diary
Project Name:  ASCII RPG
Date: 12/19

## 1. Task/Problem Description
My ASCII art doesn't look right


## 2. Initial Approach/Code
slime = [
    "  ____  ",
    " / | |\ ",
    "|   _  | ",
    "\______/ "
]
print (slime)

person = [
    "  0  ",
    " /|\\ ",
    " /|\\ ",
    "You lol"
]
print (person)

## 3. Interaction with ChatGPT
Questions/Requests to ChatGPT
Why doesn't the ASCII art print out with lines seperating them? (inserts code)

## 4. ChatGPT's Suggestions/Code Changes
ChatGPT suggested the following: Using a for loop to print each line individually

## 5. What did we learn
We learned how to print lines one at a time and I will use this to make ASCII art.

Date: 1/6/2024

## 1. Task/Problem Description
elif doesn't work, I don't know how to make a retreat function, I don't know how to reward players when they defeat an enemy, and I don't know how to subtract hp

## 2. Original Code
class slime:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    def stats(self, name, hp, attack,):
        self.name = "Green_Slime"
        self.hp = 25
        self.attack = 10
class littlegreengoober:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    def stats(self, name, hp, attack):
        self.name = "Goblin"
        self.hp = 20
        self.attack = 15


encounterchance = random.choice(randomchance)
if 10 == encounterchance:
    slime = [
    "  ____  ",
    " / | |\ ",
    "|   _  | ",
    "\______/ ",
    "You are being attacked!"
    ]
    for line in slime:
        print (line)
        incombat = True

    
if 5 == encounterchance:
    goblin_not_those_nuts = [
    " \[:(]/",
    "  / \  "
    "You are being attacked!"
    ]
    for line in goblin_not_those_nuts:
        print (line)
        incombat = True

combatoptions = [
    "1. Attack!",
    "2. Items",
    "3. Run"
]

if incombat == True:
    for line in combatoptions:
        print (line)
    combatinput = input("What would you like to do?")
    if combatinput == "1":
        #sub enemy hp - player strength
    elif combatinput == "2":
        for line in player_inventory:
            print (line)
            inventoryinput = input("What item would you like to use?")
    elif combatinput == "3":
        incombat == False
        # find a way to delete the enemy without dropping the hp to 0 so they don't get rewards

## 3. Interaction with Chat GPT
How can I fix elif, make a reward system to give players gold when they kill an enemy, make a system where the player can run from the enemy and not recieve rewards but delete the enemy from the screen and remove their influence, and finally how can I subtract hp from the enemy or myself when anything takes damage?
(Insert original code)

## 4.  Chat GPT's answer
combatoptions = [
    "1. Attack!",
    "2. Items",
    "3. Run"
]

if incombat:
    while incombat:
        for line in combatoptions:
            print(line)
        combatinput = input("What would you like to do? ")

        if combatinput == "1":  # Attack!
            # Subtract HP from enemy (or vice versa)
            if current_enemy:
                current_enemy.hp -= player_attack
                print(f"You attack the {current_enemy.name} for {player_attack} damage!")

            if current_enemy.hp <= 0:  # Enemy defeated
                print(f"You defeated the {current_enemy.name}!")
                player_gold += 50  # Reward gold for defeating the enemy
                print(f"You received 50 gold! You now have {player_gold} gold.")
                incombat = False

        elif combatinput == "2":  # Use an item
            for line in player_inventory:
                print(line)
            inventoryinput = input("What item would you like to use? ")
            # Example: Use a healing potion
            if inventoryinput == "Healing Potion":
                player_hp += 20
                print(f"You used a Healing Potion! Your HP is now {player_hp}.")
                player_inventory.remove("Healing Potion")

        elif combatinput == "3":  # Run!
            print(f"You ran from the {current_enemy.name}!")
            incombat = False  # End combat without rewards
            current_enemy = None


if not incombat:
    print("Combat is over.")


def take_damage(character, damage):
    character.hp -= damage
    print(f"{character.name} takes {damage} damage! Remaining HP: {character.hp}")


if current_enemy:
    take_damage(player_hp, current_enemy.attack)

## 5. What did I learn?
I learned how to make a simple damage system that will allow me to defeat enemies.
I learned how to reward players when they defeat an enemy
I learned how to make a system that allows the player to retreat but still not recieve rewards for running

## 1. What is the problem?
It states a boolean isn't defined

## 2. Original Code
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
        incombat = True

    
if encounterchance == 5:
    goblin_not_those_nuts = [
    " \\[:(]/",
    "  / \\  "
    "You are being attacked!"
    ]
    for line in goblin_not_those_nuts:
        print (line)
        incombat = True

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

        if combatinput == "1":  # Attack!
            # Subtract HP from enemy (or vice versa)
            if current_enemy:
                current_enemy.hp -= player_strength
                print(f"You attack the {current_enemy.name} for {player_strength} damage!")

            if current_enemy.hp <= 0:  # Enemy defeated
                print(f"You defeated the {current_enemy.name}!")
                player_money += current_enemy.reward  # Reward gold for defeating the enemy
                print(f"You received 50 gold! You now have {player_money} gold.")
                incombat = False

        elif combatinput == "2":  # Use an item
            for line in player_inventory:
                print(line)
            inventoryinput = input("What item would you like to use? ")
            # Example: Use a healing potion
            if inventoryinput == "Healing Potion":
                player_health += 20
                print(f"You used a Healing Potion! Your HP is now {player_health}.")
                player_inventory.remove("Healing Potion")

        elif combatinput == "3":  # Run!
            print(f"You ran from the {current_enemy.name} like the baby you are.")
            incombat = False  # End combat without rewards
            current_enemy = None  # Remove the enemy from the screen and influence


if not incombat:
    print("Combat is over.")

def take_damage(character, damage):
    character.hp -= damage
    print(f"{character.name} takes {damage} damage! Remaining HP: {character.hp}")

if current_enemy:
    take_damage(player_health, current_enemy.attack)

## 3. What did I ask Chat GPT
The boolean incombat isn't defined. Can you fix this? (insert code)

## 4. ChatGPT's response
import random


incombat = False  # Define the incombat variable before use
current_enemy = None
player_health = 100  # Example player's health
player_strength = 10  # Example player's attack strength
player_money = 0  # Example player's money
player_inventory = ["Healing Potion"]  # Example player's inventory


class Enemy:
    def __init__(self, name, hp, attack, reward):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.reward = reward


slime_enemy = Enemy(name="Slime", hp=50, attack=5, reward=50)
goblin_enemy = Enemy(name="Goblin", hp=40, attack=8, reward=50)


randomchance = [10, 5, 3, 2]  # Example random chance list (can add more or modify)
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
        print(line)
    current_enemy = slime_enemy
    incombat = True

elif encounterchance == 5:
    goblin_not_those_nuts = [
        " \\[:(]/",
        "  / \\  ",
        "You are being attacked!"
    ]
    for line in goblin_not_those_nuts:
        print(line)
    current_enemy = goblin_enemy
    incombat = True

combatoptions = [
    "1. Attack!",
    "2. Items",
    "3. Run"
]


if incombat:
    while incombat:
        for line in combatoptions:
            print(line)
        combatinput = input("What would you like to do? ")

        if combatinput == "1":  # Attack!
            # Subtract HP from enemy (or vice versa)
            if current_enemy:
                current_enemy.hp -= player_strength
                print(f"You attack the {current_enemy.name} for {player_strength} damage!")

            if current_enemy.hp <= 0:  # Enemy defeated
                print(f"You defeated the {current_enemy.name}!")
                player_money += current_enemy.reward  # Reward gold for defeating the enemy
                print(f"You received {current_enemy.reward} gold! You now have {player_money} gold.")
                incombat = False

        elif combatinput == "2":  # Use an item
            for line in player_inventory:
                print(line)
            inventoryinput = input("What item would you like to use? ")
            # Example: Use a healing potion
            if inventoryinput == "Healing Potion":
                player_health += 20
                print(f"You used a Healing Potion! Your HP is now {player_health}.")
                player_inventory.remove("Healing Potion")

        elif combatinput == "3":  # Run!
            print(f"You ran from the {current_enemy.name} like the baby you are.")
            incombat = False  # End combat without rewards
            current_enemy = None  # Remove the enemy from the screen and influence


if not incombat:
    print("Combat is over.")


def take_damage(character, damage):
    character.hp -= damage
    print(f"{character.name} takes {damage} damage! Remaining HP: {character.hp}")


if current_enemy:
    take_damage(player_health, current_enemy.attack)