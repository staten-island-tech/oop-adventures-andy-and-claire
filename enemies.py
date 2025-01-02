class slime:
    def __init__(self, name, hp, attack, armour, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.armour = armour
        self.speed = speed
    def stats(self, name, hp, attack, armour, speed):
        self.name = "Green_Slime"
        self.hp = 25
        self.attack = 10
        self.armour = 0
        self.speed = 5

class littlegreengoober:
    def __init__(self, name, hp, attack, armour, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.armour = armour
        self.speed = speed
    def stats(self, name, hp, attack, armour, speed):
        self.name = "Goblin"
        self.hp = 20
        self.attack = 15
        self.armour = 0
        self.speed = 10
