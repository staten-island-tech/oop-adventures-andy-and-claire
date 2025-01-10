import random
import json

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

class Enemy:
    def __init__(self, name, hp, attack, reward):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.reward = reward

class Merchant:
    def __init__(self, items):
        self.items_for_sale = {item['name']: item for item in items}

    def show_items(self):
        return list(self.items_for_sale.keys())

    def trade(self, player, item, action):
        if action == 'buy':
            if item in self.items_for_sale and player.money >= 20: 
                player.inventory.append(item)
                player.money -= 20  
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

def load_items_from_json(filename):
    """Loads items from a JSON file."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)  # Parse JSON data
            return data['items']  # Return the list of items
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []  # Return an empty list if the file doesn't exist

def game_loop():
    player_name = input("Name your character: ").strip()
    player = Player(player_name)
    current_location = town
    
    # Load items from the JSON file
    merchant_items = load_items_from_json('item.json')
    if merchant_items:  # If items were loaded successfully
        merchant = Merchant(merchant_items)
    else:
        print("No items available for the merchant.")
        return  # Exit the game if items cannot be loaded
    
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
        elif choice == "3" and current_location == town:
            in_merchant_shop = True
            print("You are talking to the merchant.")
        elif choice == "3" and current_location == forest:
            print("Returning to town")
            current_location = town
        elif choice == "4" and current_location == town:
            print(player_inventory)
            print(f"Name: {player_name} Power: {player_strength} Profits: {player_money}")
        elif choice == "4" and current_location == forest:
            current_location = town
        elif choice == "2" and current_location == forest:
            print("You search the grass")
            randomchance = [1,2,3,4,5,6,7,8,9,10]
            encounterchance = random.choice(randomchance)
            slime = Enemy(name="Slime", hp=20, attack=5, reward=20)
            goblin_not_those_nuts = Enemy(name="Goblin", hp=30, attack=10, reward=40)

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
                    current_enemy = slime
                    incombat = True

            if encounterchance == 5:
                goblin_not_those_nuts = [
                    " \\[:(]/",
                    "  / \\  ",
                    "You are being attacked!"
                ]
                for line in goblin_not_those_nuts:
                    print(line)
                    current_enemy = goblin_not_those_nuts
                    incombat = True

            else:
                print("You don't find enemies.")

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

                    if current_enemy.hp <= 0:
                        print(f"You defeated the {current_enemy.name}!")
                        player.money += current_enemy.reward
                        print(f"You received {current_enemy.reward} gold! You now have ${player.money}.")
                        incombat = False

                    elif combatinput == "2":
                        ininventory = True
                        for line in player.inventory:
                            print(line)
                            inventoryinput = input("What item would you like to use?").lower
                        if inventoryinput == "healing potion" and "healing potion" in player.inventory:
                            player.health += 20
                            print(f"You used a healing potion! Your HP is now {player.health}.")
                            player.inventory.remove("healing potion")
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
        if player.money >= 1000:
            print(f"Congratulations, {player.name}! You've won the game with ${player.money}!")
            break

        print("Game Over.")

game_loop()