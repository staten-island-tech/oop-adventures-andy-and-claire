class Player:
    def __init__(self, name, inventory, gold, ):
        self.name = name
        self.inventory = inventory
        self.gold = gold
    def buy(self, item):
        self.inventory.append(item)
        print (self.inventory)