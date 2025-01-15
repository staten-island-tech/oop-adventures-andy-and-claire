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

## 1. What is the problem?
I don't know how to delete previous code to make the game feel more alive and less like layering text on top of each other.

## 2. Previous code
No code is put here simply because I want to learn about a function

## 3. Questions asked
How can I delete previous lines in my terminal in my python ASCCII game?

## 4. ChatGPT suggestions
Clearing Lines in a Loop (Interactive Games)
If you're building an interactive game where the screen needs to be updated regularly, you can combine the techniques above to overwrite or clear lines. For example, in a text-based game, you could clear and redraw the game state every frame.

Here's an example of a simple game loop:

python
Copy code
import time
import os

def clear():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/MacOS
        os.system('clear')

def game_loop():
    score = 0
    while score < 5:
        clear()  # Clear the screen each time
        print(f"Score: {score}")
        time.sleep(1)  # Simulate some game logic
        score += 1

game_loop()
In this loop, clear() is called at the beginning of each iteration to refresh the screen, and the score is updated.

## 5. What did I learn?
I learned that I can use functions like /r, and cls for Windows when using os to clear the terminal to make my ASCCII game more interactive 

## 1. Problem
I am unsure of the possible errors in my code and I would like to make sure all my code works accordingly

## 2. Original Code
import random
import os

def clear():
    if os.name == 'nt':
        os.system('cls')

player_health = 100
player_strength = 10
player_inventory = []
player_money = 50
incombat = False
ininventory = False
current_enemy = None

character_ascii = [
    "  O  ",
    " /|\\ ",
    " / \\ ",
    " You haha "
]

merchant_ascii = [
    " [$]  ",
    " /|\\  ",
    " / \\  ",
    " Merchant "
]

class Player:
    def __init__(self, name):
        self.name = name
        self.health = player_health
        self.strength = player_strength
        self.inventory = []
        self.money = player_money

    def display_stats(self):
        return f"Health: {self.health}\nStrength: {self.strength}\nInventory: {', '.join(self.inventory) if self.inventory else 'Empty'}\nMoney: ${self.money}"

class Location:
    def __init__(self, name, description, actions, ascii_art=None):
        self.name = name
        self.description = description
        self.actions = actions
        self.ascii_art = ascii_art

    def describe(self):
        print(f"\n{self.name}: {self.description}")
        if self.ascii_art:
            for line in self.ascii_art:
                print(line)

town = Location("Town Square", "in the town full of people who don't have jobs.", ["Venture in the dark forest", "Check the quest board", "Go to the Merchant", "Look into your backpack"], [
    "  ______  ", " |      | ", " | TOWN | ", " |______| "
])

forest = Location("Dark Forest", "weird forest with monsters and herbs.", ["Pick herbs","Search the tall grass","Return to town"], [
    "   & *&&   ", "  &  * &  ", " &#  @&  && #  ", "  &   &  "
])

questboard = Location("Questboard", "The odd jobs that the town has, you're mostly interested in combat...", ["Kill_Slimes", "Kill_Goblins"], [
    " _____________________",
    "|                     |",
    "|                     |",
    "|     QUESTSBOARD     |",
    "|                     |",
    "|_____________________|"
]) 

class Quests:
    def __init__(self, task, record, prize):
        self.task = task
        self.record = record
        self.prize = prize

Kill_Goblins = Quests("Kill 5 Goblins", 0, 200)
Kill_Slimes = Quests("Kill 7 Slimes", 0, 150)

Kill_Goblins = False
Kill_Slimes = False

class enemy:
    def __init__(self, name, hp, attack, reward):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.reward = reward

def encounters():
    randomchance = [1,2,3,4,5,6,7,8,9,10]
    encounterchance = random.choice(randomchance)

    slime = enemy(name="Slime", hp=20, attack=5, reward=20)
    goblin = enemy(name="Goblin", hp=30, attack=10, reward=40)

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
            global current_enemy
            current_enemy = slime
            combat()

    
    if encounterchance == 5:
        goblin = [
            " \\[:(]/",
            "  / \\  "
            "You are being attacked!"
        ]
        for line in goblin:
            print (line)
            current_enemy = goblin
            combat()
                
    else:
        print ("You don't find enemies.")

def combat():

    Yourturn = True
    global Enemyturn
    Enemyturn = False

    combatoptions = [
        "1. Attack!",
        "2. Items",
        "3. Run"
        ]
    for line in combatoptions:
        print(line)
        combatinput = input("What would you like to do? ")

        if combatinput == "1":
            if current_enemy:
                current_enemy.hp -= player_strength
                print(f"You attack the {current_enemy.name} for {player_strength} damage!")
                Yourturn = False

                if current_enemy.hp <= 0:
                    print(f"You defeated the {current_enemy.name}!")
                    player_money += current_enemy.reward
                    print(f"You received 50 gold! You now have {player_money} gold.")
                    incombat = False
                    if current_enemy.name in "goblin" and Kill_Goblins == True:
                        Kill_Goblins.record += 1
                        if Kill_Goblins.record == 5:
                            player_money += Kill_Goblins.prize
                    if current_enemy.name in "slime" and Kill_Slimes == True:
                        Kill_Slimes.record += 1
                        if Kill_Slimes.record == 7:
                            player_money += Kill_Slimes.prize
                    current_enemy = None
                    


                elif combatinput == "2":
                    ininventory = True
                    if ininventory == True:
                        for line in player_inventory:
                            print(line)
                        inventoryinput = input("What item would you like to use?").lower
                        if inventoryinput == "healing potion" and "healing potion" in player_inventory:
                            player_health += 20
                            print(f"You used a healing potion! Your HP is now {player_health}.")
                            player_inventory.remove("healing potion")
                            Yourturn = False
                        elif inventoryinput == "q":
                            ininventory = False


                elif combatinput == "3":
                    print(f"You ran from the {current_enemy.name} like the baby you are.")
                    incombat = False 
                    current_enemy = None 
                    
                if current_enemy.hp > 0 and Yourturn == False:
                    Enemyturn = True
                    player_health -= current_enemy.attack
                    print (f"{current_enemy.name} attacked you for {current_enemy.attack}! Remaining HP:{player_health}")

    if not incombat:
        print("Combat is over.")

    def take_damage(character, damage):
        character.hp -= damage
        print(f"{character.name} takes {damage} damage! Remaining HP: {character.hp}")

    if current_enemy:
        take_damage(player_health, current_enemy.attack)

class Merchant:
    def __init__(self):
        self.items_for_sale = {"Healing Potion": 20, "Sword": 50}

    def show_items(self):
        return list(self.items_for_sale.keys())

    def trade(self, player, item, action):
        if action == 'buy':
            if item in self.items_for_sale and player.money >= self.items_for_sale[item]:
                player.inventory.append(item)
                player.money -= self.items_for_sale[item]
                return f"You bought a {item}!"
            else:
                return "Not enough money or item unavailable."
        elif action == 'sell':
            if item in player.inventory:
                player.inventory.remove(item)
                sell_price = self.items_for_sale.get(item, 10) // 2
                player.money += sell_price
                return f"You sold a {item} for ${sell_price}."
            else:
                return "You don't have that item."

def game_loop():
    player_name = input("Name your character: ").strip()
    player = Player(player_name)
    current_location = town
    merchant = Merchant()
    in_merchant_shop = False

    while True:
        print("\n-------------------------")
        print(player.display_stats())
        print("\nYour Character:")
        for line in character_ascii:
            print(line)
        print(f"{player.name}")

        current_location.describe()

        print("\nAvailable Actions:")
        for idx, action in enumerate(current_location.actions):
            print(f"{idx+1}: {action}")

        choice = input("\nChoose an action (1-4): ").strip()

        if choice == "1" and current_location == town:
            current_location = forest
        elif choice == "1" and current_location == questboard:
            print("Quest Kill Slimes has been accepted.")
            Kill_Slimes == True
        elif choice == "1" and current_location == forest:
            player.health += 10
            print("You picked some herbs and gained 10 health!")
        elif choice == "2" and current_location == town:
            print("You check the quests you can do.")
            current_location = questboard
        elif choice == "2" and current_location == forest:
            print("You search the grass")
            encounters()
        elif choice == "2" and current_location == questboard:
            print("Quest Kill Goblins has been accepted.")
            Kill_Goblins == True
        elif choice == "3" and current_location == town:
            in_merchant_shop = True
            print("You are talking to the merchant.")
        elif choice == "3" and current_location == forest:
            print("Returning to town")
            current_location = town
        elif choice == "4" and current_location == town:
            print("You leave town, left to wonder.")
            break
        elif choice == "4" and current_location == forest:
            current_location = town
        if player_money >= 1000:
            print("You are Mr.Rich Man now, congrats! Now don't screw it up like Elon did.")
            break



        if in_merchant_shop:
            print("\nMerchant Shop:")
            for line in merchant_ascii:
                print(line)
            print("Press 'b' to buy, 's' to sell, or 'q' to leave")
            action = input("What would you like to do? ").strip()

            if action == 'b':
                item = input(f"Enter the item to buy ({', '.join(merchant.show_items())}): ").strip()
                print(merchant.trade(player, item, 'buy'))
            elif action == 's':
                if player.inventory:
                    item = input(f"Enter the item to sell ({', '.join(player.inventory)}): ").strip()
                    print(merchant.trade(player, item, 'sell'))
                else:
                    print("Your inventory is empty!")
            elif action == 'q':
                in_merchant_shop = False

    print("Game Over.")

game_loop()

## 3. What question was asked to ChatGPT?
What possible errors reside in my code and how can I polish the code to make it organized? (insert code)

## 4. ChatGPT's Response
Your code has several areas where errors may arise, along with some organizational improvements that could make it more efficient and easier to maintain. I'll walk you through the main issues and suggestions for improvement:

1. Variable Re-Assignments (Line 70 & 73)
In the Kill_Goblins and Kill_Slimes lines:

python
Copy code
Kill_Goblins = False
Kill_Slimes = False
Here, you are overriding the Kill_Goblins and Kill_Slimes instances of Quests by assigning them boolean values (False). This makes the quests unavailable for the player to track. You should remove these lines.

Fix:

python
Copy code
# Remove the line that overrides the quests
# Kill_Goblins = False
# Kill_Slimes = False
2. Incorrect Comparison Operators (Line 106 & 109)
In the combat function, there are comparisons to quest conditions that use == instead of = (which is assignment, not comparison).

For example:

python
Copy code
if current_enemy.name in "goblin" and Kill_Goblins == True:
The issue is that current_enemy.name in "goblin" will always return True because the string "goblin" is being iterated over. You should compare current_enemy.name to the string "Goblin" instead.

Fix:

python
Copy code
if current_enemy.name == "Goblin" and Kill_Goblins.record == 5:
3. Variable Scope Issues with incombat and ininventory
You have variables incombat and ininventory, but you're not consistently updating them correctly, which could cause scope issues or unexpected behavior in your game loop. For example, you are setting incombat = False inside the combat() function but not handling its state properly when encountering an enemy or leaving combat.

Fix: Keep the state of incombat and ininventory properly managed to prevent issues in different areas of the game.

4. Global State and Logic Management
Your game relies heavily on global variables like player_health, player_strength, player_money, etc. This is generally not ideal because it can create confusion when the variables' state changes from multiple places. It’s best practice to manage these states inside the Player class itself.

Fix: Move all character stats into the Player class. Update the combat and merchant functionality to refer to the player's attributes through the player object.

For example:

python
Copy code
class Player:
    def __init__(self, name, health=100, strength=10, money=50):
        self.name = name
        self.health = health
        self.strength = strength
        self.money = money
        self.inventory = []

    def display_stats(self):
        return f"Health: {self.health}\nStrength: {self.strength}\nInventory: {', '.join(self.inventory) if self.inventory else 'Empty'}\nMoney: ${self.money}"
Then, update all references to player_health, player_strength, and player_money to player.health, player.strength, and player.money, respectively.

5. Combat Logic Issues (Inside combat() and encounters())
The current enemy current_enemy is a list when you create an enemy encounter but it's also referenced as an object elsewhere.
Additionally, there are issues with updating the player's health and handling combat rounds, as you're not checking properly if the player or enemy has lost.
Fix: Ensure the current_enemy is an object of the enemy class in encounters():

python
Copy code
# Correct the enemy assignment in encounters function
if encounterchance == 10:
    current_enemy = slime
    combat()

if encounterchance == 5:
    current_enemy = goblin
    combat()
Also, update the combat() function to properly handle turns and combat logic:

python
Copy code
# In combat() - Update player_health and enemy hp correctly
if combatinput == "1":
    if current_enemy:
        current_enemy.hp -= player.strength  # player attacks enemy
        print(f"You attack the {current_enemy.name} for {player.strength} damage!")

        if current_enemy.hp <= 0:
            print(f"You defeated the {current_enemy.name}!")
            player.money += current_enemy.reward  # Add reward to player's money
            print(f"You received {current_enemy.reward} gold! Your balance is now {player.money}.")

# Handle the enemy's turn
if current_enemy.hp > 0:
    player.health -= current_enemy.attack
    print(f"{current_enemy.name} attacked you for {current_enemy.attack} damage! Your HP: {player.health}")
6. Input Handling Issues
Your code has some places where input is compared directly with conditions without proper validation or handling. For example, in combat(), you ask for an input but don’t handle invalid choices (like typing something that isn’t 1, 2, or 3). You should make sure that the player's input is validated to avoid unexpected behavior.

Fix:

python
Copy code
combatinput = input("What would you like to do? ")
while combatinput not in ["1", "2", "3"]:
    print("Invalid choice. Please select a valid option.")
    combatinput = input("What would you like to do? ")
7. Class Organization
The code could be made more organized by grouping related functionalities into relevant classes. For example, creating a Game class that manages the entire game loop, combat system, and the player's interactions with NPCs (such as merchants). This would help separate concerns and make the code easier to extend.

Suggestion:

python
Copy code
class Game:
    def __init__(self):
        self.player = None
        self.current_location = None
        self.merchant = Merchant()

    def start_game(self):
        self.player = Player(input("Enter your character name: ").strip())
        self.current_location = town
        # Then, continue with the main game loop here...
8. Error Handling and Code Flow
If the player decides to buy or sell an item, the transaction is handled, but there is no error handling for invalid actions.
Also, after selling or buying, you should print feedback to the player, so they understand what just happened.
Fix: Improve error handling and feedback for transactions in the merchant section.

## 5. What did I learn?
I learned I have a whole handful of problems and I need to fix them while getting possible solutions to these problems
