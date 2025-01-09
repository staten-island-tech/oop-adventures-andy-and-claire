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
            #Make quests a thing in this game
        elif choice == "3" and current_location == town:
            in_merchant_shop = True
            print("You are talking to the merchant.")
        elif choice == "3" and current_location == forest:
            print("Returning to town")
            current_location = town
        elif choice == "4" and current_location == town:
            print(player_inventory)
            print (f"Name: {player_name} Power: {player_strength} Profits: {player_money}")
        elif choice == "4" and current_location == forest:
            current_location = town
        elif choice == "2" and current_location == forest:
            print("You search the grass")
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