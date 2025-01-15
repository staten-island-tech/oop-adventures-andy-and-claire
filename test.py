import random
import time
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

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
    def __init__(self, name, health, strength, inventory, money):
        self.name = name
        self.health = health
        self.strength = strength
        self.inventory = inventory
        self.money = money

    def display_stats(self):
        return f"Health: {self.health}\nStrength: {self.strength}\nInventory: {', '.join(self.inventory) if self.inventory else 'Empty'}\nMoney: ${self.money}"

    def take_damage(self,damage):
        player.health -= damage
        print(f"{player.name} takes {damage} damage! Remaining HP: {player.health}")

player = Player("",100,10,[],50)

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

town = Location("Town Square", "in the town full of people who don't have jobs.", ["Venture in the dark forest", "Check the quest board", "Go to the Merchant", "Go to the inn"], [
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

inn = Location("Inn", "Here you can rest, You better treasure it.", ["Take a rest for 5 gold", "Leave"], [
    " _______ ",
    "|       |"
    "|  Inn  |",
    "|_______|"
])

class Quests:
    def __init__(self, task, record, prize, activate):
        self.task = task
        self.record = record
        self.prize = prize
        self.activate = activate

Kill_Goblins = Quests("Kill 5 Goblins", 0, 200, False)
Kill_Slimes = Quests("Kill 7 Slimes", 0, 150, False)

class enemy:
    def __init__(self, name, hp, attack, reward):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.reward = reward

def combat():
    randomchance = [1,2,3,4,5,6,7,8,9,10]
    encounterchance = random.choice(randomchance)

    current_enemy = None

    slime = enemy("Slime", 20, 5, 20)
    goblin = enemy("Goblin", 30, 10, 40)

    if encounterchance == 10:
        print("  ____  \n / | |\\ \n|   _  | \n\\______/ \nYou are being attacked by a slime!")
        current_enemy = slime

    
    if encounterchance == 5:
        print(" \\[:(]/\n  / \\  \nYou are being attacked by a goblin!")
        current_enemy = goblin

    else:
        print ("You don't find enemies.")
        return

    combatoptions = [
        "1. Attack!",
        "2. Items",
        "3. Run"
        ]
    print(combatoptions)
    combatinput = input("What would you like to do? ")

    if combatinput == "1":
        if current_enemy:
            current_enemy.hp -= player.strength
            print(f"You attack the {current_enemy.name} for {player.strength} damage!")

            if current_enemy.hp > 0:
                player.health -= current_enemy.attack
                print (f"{current_enemy.name} attacked you for {current_enemy.attack}! Remaining HP:{player.health}")

            if current_enemy.hp <= 0:
                print(f"You defeated the {current_enemy.name}!")
                player.money += current_enemy.reward
                print(f"You received 50 gold! You now have {player.money} gold.")
                if current_enemy.name == "Goblin" and Kill_Goblins.activate == True:
                    Kill_Goblins.record += 1
                    if Kill_Goblins.record == 5:
                        player.money += Kill_Goblins.prize
                if current_enemy.name == "slime" and Kill_Slimes.activate == True:
                    Kill_Slimes.record += 1
                    if Kill_Slimes.record == 7:
                        player.money += Kill_Slimes.prize
                current_enemy = None
                return current_enemy
                    


    elif combatinput == "2":
        for line in player.inventory:
            print(line)
        if player.inventory == []:
            print("I'm sorry but it seems that your inventory is empty. Please type q to exit inventory")
        inventoryinput = input("What item would you like to use? Type q to exit your inventory").lower()
        if inventoryinput == "healing potion" and "healing potion" in player.inventory:
            player.health += 20
            print(f"You used a healing potion! Your HP is now {player.health}.")
            player.inventory.remove("healing potion")
        elif inventoryinput == "q":
            print("Exiting inventory")
            clear()
            print(combatoptions)
            combatinput = input("What would you like to do?")


    elif combatinput == "3":
        print(f"You ran from the {current_enemy.name} like the baby you are.")
        current_enemy = None
        return current_enemy
        
    elif combatinput not in ["1","2","3"]:
        print("Invalid answer, please choose an answer provided")
        time.sleep(1)
        clear()
        print (combatoptions)
        combatinput = input("What would you like to do?")
    if player.health <= 0:
        print("You die in the heat of the fight, Try again?")

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
        else:
            print("That is not a valid option, please choose one from the options provided.")

def game_loop():
    player.name = input("Name your character: ").strip()
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
            print("Traveling to the dark forest")
            time.sleep(1)
            clear()
            current_location = forest
        elif choice == "1" and current_location == questboard:
            print("Quest Kill Slimes has been accepted.")
            Kill_Slimes.activate = True
            time.sleep(1)
            clear()
            current_location = town
        elif choice == "1" and current_location == forest:
            player.health += 10
            print("You picked some herbs and gained 10 health!")
            time.sleep(1)
            clear()
        elif choice == "1" and current_location == inn:
            player.health = 100
            player.money -= 5
            print("You rest well.")
            time.sleep(1)
            clear()
            current_location = town
        elif choice == "2" and current_location == town:
            clear()
            print("You check the quests you can do.")
            current_location = questboard
        elif choice == "2" and current_location == forest:
            print("You search the grass")
            combat()
            time.sleep(1)
            clear()
        elif choice == "2" and current_location == questboard:
            print("Quest Kill Goblins has been accepted.")
            Kill_Goblins.activate = True
            time.sleep(1)
            clear()
        elif choice == "2" and current_location == inn:
            print("You left the inn.")
            time.sleep(1)
            clear()
            current_location = town
        elif choice == "3" and current_location == town:
            clear()
            in_merchant_shop = True
            print("You are talking to the merchant.")
        elif choice == "3" and current_location == forest:
            print("Returning to town")
            time.sleep(1)
            clear()
            current_location = town
        elif choice == "4" and current_location == town:
            print("You enter the inn")
            time.sleep(1)
            clear()
        elif choice == "4" and current_location == forest:
            print("Returning to Town")
            time.sleep(1)
            clear()
            current_location = town
        if player.health <= 0:
            print("You unfortuantly die, Try again?")
            break
        if player.money > 1000:
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