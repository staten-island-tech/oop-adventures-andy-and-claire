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

## 5. What did I learn?
I learned how to access my data and leave no "deadcode"

## 1. What's the issue?
I would like to check my code for errors

## 2. Previous code
import random


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
    goblin_not_those_nuts = enemy(name="Goblin", hp=30, attack=10, reward=40)

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

def combat():

    Yourturn = True
    Enemyturn = False

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
                            print(f"You attack the {current_enemy.name} for {player_strength} damage!")
                            Yourturn = False

                    if current_enemy.hp <= 0:
                        print(f"You defeated the {current_enemy.name}!")
                        player_money += current_enemy.reward
                        print(f"You received 50 gold! You now have {player_money} gold.")
                        incombat = False

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

    if incombat == False:
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
        elif choice == "1" and current_location == forest:
            player.health += 10
            print("You picked some herbs and gained 10 health!")
        elif choice == "2" and current_location == town:
            print("You check the quests you can do.")
            #Make quests
        elif choice == "2" and current_location == forest:
            print("You search the grass")
            encounters()
            if incombat == True:
                combat()
        elif choice == "3" and current_location == town:
            in_merchant_shop = True
            print("You are talking to the merchant.")
        elif choice == "3" and current_location == forest:
            print("Returning to town")
            current_location = town
        elif choice == "4" and current_location == town:
            print("You left town")
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

## 3. What did I ask ChatGPT?
Are there any errors in my code I should be aware of?

## 4. ChatGPT's response
Your code is generally well-structured, but there are several areas where potential issues could arise. Below, I've highlighted key points and possible errors to watch out for:

1. current_enemy and incombat Scope
Problem: You're modifying current_enemy and incombat within functions, but these variables are defined globally. Modifying them locally does not affect the global state.
Solution: Use the global keyword to modify these variables inside the functions or consider passing them as arguments to functions.
For example:

python
Copy code
global current_enemy, incombat
current_enemy = slime
incombat = True
2. Inventory Input Error
Problem: In the combat function, the inventoryinput is assigned incorrectly, missing parentheses on the .lower() method. This causes a TypeError as you're trying to assign a method instead of calling it.
Solution: Add parentheses to the lower() call:
python
Copy code
inventoryinput = input("What item would you like to use?").lower()
3. Use of random.choice() for Encounters
Problem: You're choosing an encounter with a fixed list [1, 2, 3, ..., 10], which works fine for generating random numbers. However, this can be simplified by choosing a random number in a specific range.
Solution: Use random.randint() to generate a random number directly:
python
Copy code
encounterchance = random.randint(1, 10)
4. Combat Logic - Switching Turns
Problem: The combat system has logic to switch turns between the player and the enemy, but you're not effectively managing the turn order. Yourturn and Enemyturn are not used consistently, which might cause unexpected behavior.
Solution: Simplify the combat turn management. For example:
python
Copy code
if combatinput == "1" and current_enemy:
    current_enemy.hp -= player_strength
    print(f"You attack the {current_enemy.name} for {player_strength} damage!")
    if current_enemy.hp <= 0:
        print(f"You defeated the {current_enemy.name}!")
        player.money += current_enemy.reward
        incombat = False
        continue  # Skip to the next loop iteration

if current_enemy.hp > 0:
    # Enemy attacks after player
    player.health -= current_enemy.attack
    print(f"{current_enemy.name} attacks you for {current_enemy.attack} damage!")
    print(f"Remaining HP: {player.health}")
5. Misplaced take_damage Function
Problem: The take_damage() function is nested inside the combat() function, but it doesn't seem to be called in a way that makes sense. It also takes character as an argument but is designed to modify character.hp, which is somewhat unclear.
Solution: Move take_damage outside the combat() function, or make sure it is integrated correctly.
Example:

python
Copy code
def take_damage(character, damage):
    character.hp -= damage
    print(f"{character.name} takes {damage} damage! Remaining HP: {character.hp}")
6. Merchant Inventory Interaction
Problem: You're checking if the player has enough money to buy an item from the merchant, but the player.money is not being updated properly when the player buys an item.
Solution: The player.money should be updated inside the trade method. You're already doing this, so ensure the return messages accurately reflect whether or not the transaction was successful.
7. Missed String Formatting
Problem: Some print statements are not properly formatted, making them harder to read or causing errors.
Solution: Consider using f-strings for consistent formatting, such as:
python
Copy code
print(f"You received {current_enemy.reward} gold! You now have {player.money} gold.")
8. Lack of Proper Break in Combat Loop
Problem: After defeating an enemy, you should break out of the combat loop immediately to avoid unnecessary turns.
Solution: Add a break statement after the player defeats the enemy:
python
Copy code
if current_enemy.hp <= 0:
    print(f"You defeated the {current_enemy.name}!")
    player.money += current_enemy.reward
    print(f"You received {current_enemy.reward} gold!")
    incombat = False
    break  # Exit combat loop
9. Logical Issue with current_location
Problem: In the game loop, the player's location is changed when specific choices are made, but the current_location comparison might break when moving between areas like the town and forest.
Solution: Use more explicit checks or methods to move between locations, and ensure that the state is managed correctly when transitioning between locations.
Minor Fixes and Improvements:
Inconsistent indentation in some places. Ensure consistent indentation throughout the code (e.g., 4 spaces).
The combat loop can be simplified and refactored for better clarity, ensuring that the player's turn and the enemy's turn are handled more clearly.
Ensure that you handle cases like empty inventories or items not available for buying or selling, providing appropriate feedback.
Final Thoughts:
After addressing these points, the game should run more smoothly and be more readable. Feel free to refine further based on your specific game design and logic. Let me know if you need any more specific help with any of these areas!
## 5. What I learned
Ok... I need to practice coding
Like
Holy Cow there are so many problems
Ok. Where to start. I learned how to use global and it's purpose in code, to update data on all code