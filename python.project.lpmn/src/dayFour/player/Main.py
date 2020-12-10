from Player import *
import pickle  

name = str(input("What your name ?\n"))
level = int(input("What your level ?\n"))

playerOne = Player(name,level)

with open("player.txt", "wb") as file:
    record = pickle.Pickler(file)
    record.dump(playerOne)

with open("player.txt", "rb") as file:
    get_record = pickle.Unpickler(file)
    playerOne = get_record.load()

playerOne.whoami()