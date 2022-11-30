gearchoice = 0
shopchoice = 0
citychoice = 0
def gearshop(gearchoice, dmg, gold, hp):
    gearchoice = input("this is a basic gear shop, you can upgrade either your sword or armor here, which would you like?")
    if gearchoice == "sword" and gold >= 50:
        dmg = dmg + 1
        gold = gold - 50
    if gearchoice == "armor" and gold >= 50:
        hp = hp + 8
        gold = gold - 50
    else:
        print("sorry, you can't afford it")
        print("you should go for a quest")
        spawn(pmonster)
def shop(shopchoice, hp):
    shopchoice = input("would you like a health potion, yes/no?")
    if shopchoice == "yes" and hp >= hp - 16:
        print("here you go, drink up")
        hp = hp + 16
        print("have a good day")
        threepaths()
    else:
        print("sorry, but you currently cant get one at the moment")
        spawn(pmonster)
def city(citychoice, hp):
    print("you have visited a nearby city, what would you like to do?")
    citychoice1 = input("would you like to buy some items? if yes, please type *items* if you dont, do you want to buy some gear, if yes, please type *shop* else, you can get some rest, note, you can only do one of these things")
    if citychoice == "items" or "*items*":
        shop()
    if citychoice == "shop" or "*shop*":
        gearshop()
    else:
        print("you go to bed for the day at am inn")
        hp = hp + 2 * level
    threepaths()
