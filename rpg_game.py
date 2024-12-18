import sys

# Game variables
player_name = "Hero"
player_health = 100
player_strength = 10
player_inventory = []
player_money = 50  # Starting money

enemy_health = 90  # Monster's health

# Define the Player class
class Player:
    def __init__(self, name, health, strength, money):
        self.name = name
        self.health = health
        self.strength = strength
        self.inventory = []
        self.money = money

    def display_stats(self):
        health_text = f"Health: {self.health}"
        strength_text = f"Strength: {self.strength}"
        inventory_text = f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}"
        money_text = f"Money: ${self.money}"
        return health_text, strength_text, inventory_text, money_text

# Set up locations and actions
class Location:
    def __init__(self, name, description, actions, ascii_art=None):
        self.name = name
        self.description = description
        self.actions = actions
        self.ascii_art = ascii_art

    def describe(self):
        return f"\n{self.name}: {self.description}"

    def show_ascii_art(self):
        if self.ascii_art:
            for line in self.ascii_art:
                print(line)

# Create some locations with ASCII Art
town_ascii = [
    "  _____  ",
    " |     | ",
    " | TOWN | ",
    " |_____| "
]

forest_ascii = [
    "   &&&   ",
    "  &   &  ",
    " &&  &&  ",
    "  &   &  "
]

town = Location("Town Square", "You are in a busy town square. People are walking around.", 
                ["Go to the Inn", "Speak to the blacksmith", "Go to the Merchant", "Leave the town"], town_ascii)
forest = Location("Dark Forest", "The forest is dark and full of eerie sounds. It's quiet.", 
                  ["Fight a monster", "Pick herbs", "Return to town"], forest_ascii)

# Merchant class to handle buying and selling
class Merchant:
    def __init__(self):
        self.items_for_sale = {"Healing Potion": 20, "Sword": 50}

    def show_items(self):
        return list(self.items_for_sale.keys())

    def buy_item(self, player, item):
        if item in self.items_for_sale and player.money >= self.items_for_sale[item]:
            player.inventory.append(item)
            player.money -= self.items_for_sale[item]
            return f"You bought a {item}!"
        else:
            return "You can't afford that item or it's not available."

    def sell_item(self, player, item):
        if item in player.inventory:
            player.inventory.remove(item)
            sell_price = self.items_for_sale.get(item, 10) // 2  # Sell for half the buy price
            player.money += sell_price
            return f"You sold a {item} for ${sell_price}."
        else:
            return "You don't have that item to sell."

# Main game loop
def game_loop():
    global player_health, player_strength, player_inventory, player_name, enemy_health, player_money
    player = Player(player_name, player_health, player_strength, player_money)
    current_location = town
    merchant = Merchant()

    in_merchant_shop = False  # To track if we're inside the merchant shop

    running = True
    while running:
        print("\n-------------------------")
        # Display player stats
        health_text, strength_text, inventory_text, money_text = player.display_stats()
        print(health_text)
        print(strength_text)
        print(inventory_text)
        print(money_text)

        # Display the location and description
        print(current_location.describe())

        # Show ASCII Art for the current location
        current_location.show_ascii_art()

        # Handle merchant shop interaction
        if in_merchant_shop:
            print("\nMerchant Shop:")
            print("Press 'b' to buy, 's' to sell, or 'q' to leave")
            items = merchant.show_items()
            for i, item in enumerate(items):
                print(f"{i+1}: {item} - ${merchant.items_for_sale[item]}")

        # Player input for actions
        print("\nAvailable Actions:")
        for i, action in enumerate(current_location.actions):
            print(f"{i+1}: {action}")

        # Get player's choice
        choice = input("\nChoose an action (1-4): ").strip()

        if choice == "1":
            if current_location == town:
                current_location = forest
            elif current_location == forest:
                # Fight monster (simplified example)
                if enemy_health > 0:
                    player.health -= 10  # Player takes damage
                    enemy_health -= 20  # Monster takes damage
                    player.inventory.append("Monster's Fang")
                    print("You fought a monster!")
        elif choice == "2":
            if current_location == town:
                print("You speak to the blacksmith.")
            elif current_location == forest:
                print("You gather herbs.")
        elif choice == "3":
            if current_location == town:
                # Enter merchant shop
                in_merchant_shop = True
                print("You are talking to the merchant.")
            elif current_location == forest:
                current_location = town
        elif choice == "4":
            if current_location == town:
                print("You leave the town.")
                running = False  # End the game
            elif current_location == forest:
                current_location = town

        # Merchant shop actions
        if in_merchant_shop:
            merchant_action = input("\nEnter 'b' to buy, 's' to sell, or 'q' to leave: ").strip().lower()
            if merchant_action == 'b':
                # Buy item logic
                items = merchant.show_items()
                print("\nAvailable items to buy:")
                for i, item in enumerate(items):
                    print(f"{i+1}: {item} - ${merchant.items_for_sale[item]}")
                item_choice = input("\nEnter the number of the item you want to buy: ").strip()
                try:
                    item_index = int(item_choice) - 1
                    if 0 <= item_index < len(items):
                        item = items[item_index]
                        print(merchant.buy_item(player, item))
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input.")
            elif merchant_action == 's':
                # Sell item logic
                if player.inventory:
                    print("\nYour inventory:")
                    for i, item in enumerate(player.inventory):
                        print(f"{i+1}: {item}")
                    item_choice = input("\nEnter the number of the item you want to sell: ").strip()
                    try:
                        item_index = int(item_choice) - 1
                        if 0 <= item_index < len(player.inventory):
                            item = player.inventory[item_index]
                            print(merchant.sell_item(player, item))
                        else:
                            print("Invalid choice.")
                    except ValueError:
                        print("Invalid input.")
                else:
                    print("Your inventory is empty!")
            elif merchant_action == 'q':
                in_merchant_shop = False  # Leave merchant shop
            else:
                print("Invalid choice.")
            
        # Check for player or enemy death
        if player.health <= 0:
            print("You have been defeated!")
            running = False
        elif enemy_health <= 0:
            print("You defeated the enemy!")
            enemy_health = 90  # Reset enemy health after defeat

# Start the game loop
game_loop()

print("Game Over.")
