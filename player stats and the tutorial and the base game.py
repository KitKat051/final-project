#player stats
import random
level = 1
level = int(level)
hp = 0
AC = 0
def d6():
    random.randint(1,6)
hp = (8 * level)
atkdmg = d6() + (level // 2)
AC = 12 + (level // 5)

#beginning of the game
choice = 0
def tutorial():
    print("alright, since I do not know how to make a seperate screen, ill just tell you how this game works")
    print("this game is a basic rpg, all you do is walk a lonley path, fight monsters, and do events, and thats about it.")
    print("this was meant to be a test run of a game to see if I can make something even a little entertaining, oh, sorry for that tangent, back to the tutorial")
    print("the basics are that you will find a crossroads, and you can choose one of three things, you can either fight a monster, go to an event, or go to a city. there might be more later")
    print("once you pick a path, you can go through the choice you have made, with monsters, combat is automatic, you only need to give your input on if you want to attack the creature, or run. this loop continues until one of you either dies or runs away, if you win, you will recieve a currency known as gold, and xp, more on those later")
    print("for events, you will be told of an incident, and you can choose whether to help out, steal, or nothing at all. for cities, you spend gold here to either get better gear, rest, and heal.")
    print("xp is used for leveling up, leveling up increases all basic stats, though leveling up cost more every five levels.")
    print("and thats about it for now I guess, have fun")
threepaths()    
print("welcome to this random game, you are running this game, so I imagine you want to play it.")
choice = input("do you want a tutorial? yes / no ?")
if choice == "yes":
    tutorial()
else:
    threepaths()
