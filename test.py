import json

player_health = 100
player_strength = 10
player_inventory = []
player_money = 50

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
    with open('items.json', 'r') as file:
        data = json.load(file)
    return data['items']

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

town = Location("Town Square", "in the town full of people who don't have jobs.", ["Go to the Forest", "Speak to the blacksmith", "Go to the Merchant", "Leave the town"], [
    "  ______  ", " |      | ", " | TOWN | ", " |______| "
])

forest = Location("Dark Forest", "weird forest with monsters and herbs.", ["Pick herbs", "Return to town"], [
    "   & *&&   ", "  &  * &  ", " &#  @&  && #  ", "  &   &  "
])

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
            player.health += 10
            print("You picked some herbs and gained 10 health!")
        elif choice == "2" and current_location == town:
            print("You speak to the blacksmith.")
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

    print("Game Over.")

game_loop()
