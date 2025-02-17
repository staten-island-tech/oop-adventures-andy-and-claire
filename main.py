import random
import json
import os
import time

def clear():
    if os.name == 'nt':
        os.system('cls')  

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

def load_items_from_json():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        return data['items']  
    except FileNotFoundError:
        print("Error: 'items.json' file not found.")
        return []

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 10
        self.inventory = []
        self.money = 50

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

forest = Location("Dark Forest", "weird forest with monsters and herbs.", ["Pick herbs", "Search the tall grass", "Return to town"], [
    "   & *&&   ", "  &  * &  ", " &#  @&  && #  ", "  &   &  "
])

class Enemy:
    def __init__(self, name, hp, attack, reward):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.reward = reward

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! Remaining HP: {self.hp}")
    
    def is_dead(self):
        return self.hp <= 0

def combat(player, enemy):
    combat_options = [
        "1. Attack!",
        "2. Items",
        "3. Run"
    ]
    
    while not enemy.is_dead() and player.health > 0:
        print("\nCombat options:")
        for option in combat_options:
            print(option)
        
        action = input("What will you do? (1/2/3): ").strip()

        if action == "1":
            enemy.take_damage(player.strength)
            if enemy.is_dead():
                print(f"You defeated the {enemy.name}!")
                player.money += enemy.reward
                print(f"You received {enemy.reward} gold! Your total money is now {player.money}.")
                return
            player.health -= enemy.attack
            print(f"{enemy.name} attacks you for {enemy.attack} damage. Your remaining health: {player.health}")
        
        elif action == "2":
            if player.inventory:
                print("\nYour Inventory:")
                for idx, item in enumerate(player.inventory, 1):
                    print(f"{idx}. {item}")
                item_choice = input("Select an item to use or type 'q' to cancel: ").strip()
                if item_choice.lower() == "q":
                    continue
                try:
                    item = player.inventory[int(item_choice) - 1]
                    if item == "Healing Potion":
                        player.health += 20
                        print(f"You used a {item}. Your health is now {player.health}.")
                        player.inventory.remove(item)
                    else:
                        print("Invalid item.")
                except (ValueError, IndexError):
                    print("Invalid selection.")
            else:
                print("You don't have any items.")
        
        elif action == "3":
            print(f"You ran from the {enemy.name}.")
            return

        else:
            print("Invalid input, please choose from the available options.")
    
    if player.health <= 0:
        print("You have been defeated!")

class Merchant:
    def __init__(self, items):
        self.items_for_sale = {item['name']: item for item in items}

    def show_items(self):
        return list(self.items_for_sale.keys())

    def trade(self, player, item, action):
        if action == 'buy':
            if item in self.items_for_sale and player.money >= self.items_for_sale[item]['price']: 
                player.inventory.append(item)
                player.money -= self.items_for_sale[item]['price']
                return f"You bought a {item}!"
            else:
                return "Not enough money or item unavailable."
        elif action == 'sell':
            if item in player.inventory:
                player.inventory.remove(item)
                sell_price = 10  
                player.money += sell_price
                return f"You sold a {item} for ${sell_price}."
            else:
                return "You don't have that item."

def game_loop():
    items = load_items_from_json()
    merchant = Merchant(items)
    
    player_name = input("Name your character: ").strip()
    player = Player(player_name)
    current_location = town
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
            encounter_chance = random.choice([True, False])  
            if encounter_chance:
                enemy = Enemy(name="Goblin", hp=30, attack=10, reward=50)
                print(f"A {enemy.name} has appeared!")
                combat(player, enemy)
            else:
                player.health += 10  
                print("You picked some herbs and gained 10 health!")
        elif choice == "2" and current_location == town:
            print("You check the quest board.")
        elif choice == "2" and current_location == forest:
            print("You gather herbs.")
        elif choice == "3" and current_location == town:
            in_merchant_shop = True
            print("You are talking to the merchant.")
        elif choice == "3" and current_location == forest:
            current_location = town
        elif choice == "4" and current_location == town:
            print("You leave the town.")
            break
        elif choice == "4" and current_location == forest:
            current_location = town

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

        clear()  

    print("Game Over.")

game_loop()
