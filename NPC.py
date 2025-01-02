class walking_store:
    def __init__(self, item, price, gold):
        self.item = item
        self.price = price
        self.gold = gold
        gold = 500
    def sell(self, item, price, gold):
        self.item.remove(item)
        self.gold.add(gold + price) 
    def buy(self, item, price, gold):
        self.item.append(item)
        self.gold.subtract(gold - price)