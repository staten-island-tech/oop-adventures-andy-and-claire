# ChatGPT Coding Diary
Project Name: 
Date: 12/19

## 1. Task/Problem Description
To create a game in the terminal similar to a text based game style. A hero will be able to navigate in places to buy items and defeat enemies.

## 2. Initial Approach/Code
We started off with the hero class to define its name, health, strength and money. We started off the player with a certain amount of everything. We also wanted to include ascii art into it but didn't know how to. I made a location function.

class Player:
    def __init__(self, name):
        self.name = name
        self.health = player_health
        self.strength = player_strength
        self.inventory = []
        self.money = player_money

class Location:
    def __init__(self, name, description, actions, ascii_art=None):
        self.name = name
        self.description = description
        self.actions = actions
        self.ascii_art = ascii_art

## 3. Interaction with ChatGPT
Questions/Requests to ChatGPT
I asked it to make ascii art for the locations. I asked how to make merchant class using items from JSON (items.json was made by Andy so we had to combine both of our code). The merchant allow the player to buy items from it or sell items. At first we didnt have a JSON file so we just defined the items but once we had the items, we used the JSON file combined with what the merchant already did. Also I wanted to make it so when we press a key, it would do a action.

I asked a few questions once they helped me make the main game loop. Some questions I asked was "what is .strip()?" 

## 4. ChatGPT's Suggestions/Code Changes
ChatGPT suggested the following:
The .strip() method in Python is used to remove any leading (beginning) and trailing (end) whitespace characters from a string. These whitespace characters can include spaces, tabs, and newline characters. It does not remove whitespace from the middle of the string.

The acsii art:
town = Location("Town Square", "in the town full of people who don't have jobs.", ["Go to the Forest", "Speak to the blacksmith", "Go to the Merchant", "Leave the town"], [
    "  _____  ", " |     | ", " | TOWN | ", " |_____| "
])

forest = Location("Dark Forest", "weird forest with monsters and herbs.", ["Pick herbs", "Return to town"], [
    "   & *&&   ", "  &  * &  ", " &#  @&  && #  ", "  &   &  "
])

BEFORE JSON:
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
            sell_price = self.items_for_sale.get(item, 10) // 2  # Sell for half the price
            player.money += sell_price
            return f"You sold a {item} for ${sell_price}."
        else:
            return "You don't have that item to sell."
AFTER JSON:
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

Keyboard with game:
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

## 5. What did we learn
- It helped me learn the basics of creating a text-based game and using classes,JSON and user input. 
- We learned how to integrate JSON data into the game. We learned how to allow the player to interact with the world, the core of a text based game. 
- Using methods like .strip() makes the game work better. 
- Use different locations and how the player moves. 
- Using if and elif to manage actions like moving between locations or buying/selling items. Design game mechanics. 
- Overall, this project taught us to structure a text based game to manage user input efficiently. 