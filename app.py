import json
import os
Player = open("./Player.json", encoding="utf8")
playerdata = json.load(Player)

class new_player:
    def __init__(self, name):
        self.name = name
    def new_player():
        name = input("Enter name: ")
        return new_player(name)
    
player = new_player.new_player()
print (new_player.__dict__)