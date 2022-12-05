import random
import time
attack = 20
mon = 0
#goblin stats
ghit = 0
ghp = 0
gdmg = 0
gattack = 0
gAC = 10
gattacks = 0
#orc stats
Ohit = 0
Odmg = 0
Oattack = 0
Ohp = 0
OAC = 0
#goblin horde stats
GHhit = 0
GHhp = 0
GHdmg = 0
GHattack = 0
ghAC = 0
#orc squad stats
OShit = 0
OShp = 0
OSdmg = 0
OSattack = 0
osAC = 0
#wyrm stats
Whit = 0
Whp = 0
Wdmg = 0
Wattack = 0
WAC = 0
# other variables
spawn_monster = 0
d20 = 0
d6 = 0
ylevel = int(1)
xpcost = 1
xp = 0
gold = 50
hp = 60
atkdmg = 6 + (ylevel // 2)
AC = 12 + (ylevel // 5)
gearchoice = 0
shopchoice = 0
citychoice = 0
dmgtaken = 0
hpp = 0
monsters = ['Goblin', 'Orc', 'Goblin-horde', 'Orcsquad', 'wyrm']
pmonsters = ['Goblin', 'Orc', 'Goblin-horde', 'Orcsquad']
spawn_monster == random.randint(1,2)
# def level(ylevel, xp, xpcost):
 #   if xp >= (100 * xpcost):
#        ylevel += 1
#        print("you level up")
#    if ylevel >= 4:
 #      xpcost = 1
  #      ylevel = (XP / (100 * xpcost))
#    if ylevel <= 5 and level >= 9:
#        xpcost = 2
#        ylevel = (XP / (100 * xpcost))
#    if ylevel <= 10 and level >= 15:
#        xpcost = 3
#        ylevel = (XP / (100 * xpcost))
#    if ylevel <= 16 and level >= 19:
#        xpcost = 4
#        ylevel = (XP / (100 * xpcost))
#    if ylevel == 20:
#        xpcost = 100000
#        ylevel = (XP / (100 * xpcost))

def d20(d20):
    d20 = random.randint(1,20)
    return d20
def d6(d6):
    d6 = random.randint(1,6)
    return d6
#beginning of the game
choice = 0
def threepaths(spawn, events, city, hp, xp):
    print(hp)
    threechoice = input("you have reached a fork in your methiphorical road of life, what would you like to do? do you want to go to a city? or do you want to explore? or do you want to kill some monsters! to go to a city, type city, to go and explore, type event, and to fight monsters, type monster ")
    if threechoice == "city":
        city(citychoice, hp)
        print("city")
    if threechoice == "monster":
        print(hp)
        spawn(pmonsters, hp, xp)
        print("monster")
    if threechoice == "event":
        event(d10, dmgtaken, gold, hp, xp)


d10 = 0
def d10(d10):
    d10 = random.randint(1,10)
    return d10
def event(d10, dmgtaken, gold, hp, xp):
    d10 = random.randint(1,5)
    if d10 == 1:
        print("it's a trap!")
        time.sleep(1)
        print("you have steped in a punji trap")
        dmgtaken = random.randint(4,12)
        time.sleep(1)
        print("you have taken", dmgtaken, "damage")
        hp = hp - dmgtaken
        print(hp, "total hp left")
        if hp <= 0:
            print("you have died to a hunting trap, atleast it was not a goblin")
        else:
            threepaths(spawn, event, city, hp, xp)
    elif d10 == 2:
        print("you have found a wandering monster")
        spawn(pmonsters, hp, xp)
    elif d10 == 3:
        print("you have found an abandonded mine, what do you want to do")
        time.sleep(1)
        minechoice = input("do you want to explore it? yes/no")
        if minechoice == "yes":
            mine = random.randint(1,2)
            if mine == 1:
                print("you have struck gold")
                gold = gold + 100
                threepaths(spawn, event, city, hp, xp)
            if mine == 2:
                print("you have found nothing, not surprising")
                threepaths(spawn, event, city, hp, xp)
        else:
            print("you have decided to leave the mine, no use in wasting time")
            threepaths(spawn, event, city, hp, xp)
    elif d10 == 4:
        appletree = input("you see an orchard, do you want to have a look around no one else is here? yes/no")
        if appletree == "yes":
            apple = input("you can either eat the apples now or sell them later, do you want to eat them now? yes/no")
            if apple == "yes":
                hp = hp + (5 * ylevel)
                print("the apple taste like an apple, your welcome")
                print("you heal")
                hpp = (5 * ylevel)
                print(hp + hpp)
                threepaths(spawn, event, city, hp, xp)
            else:
                print("you sell the apple")
                gold = gold + 30
                print("you get 30 gold")
                threepaths(spawn, event, city, hp, xp)
        else:
            print("you leave the orchard without taking anything, what a good guy you are.")
            threepaths(spawn, event, city, hp, xp)
    elif d10 == 5:
        kitten = input("you see a kitten on the side of the road, he is meowing at you, do you want to pet it? yes/no")
        if kitten == "yes":
            print("you pet the kitten")
            threepaths(spawn, event, city, hp, xp)
        else:
            print("you do not pet the kitten")
            threepaths(spawn, event, city, hp, xp)
    

def Goblin(ghit, ghp, gdmg, gattack, gAC, d20, gold, xp, hp, attack, AC):
    ghit = 2
    ghp = 12
    gdmg = 3
    gatttack = d20(d20) + ghit
    gAC = 10
    print(hp, "total hp left")
    choice = input("you encounter a Goblin, what do you want to do? do you want to attack? yes/no?")
    if choice == "yes":
        battle = False
        done = False
        while not done:
            print("rolling d20") 
            if attack >= gAC:
                ghp = ghp - atkdmg
                print("you dealt", atkdmg, "damage")
                time.sleep(1)
                if ghp <= 0:
                    print("the Goblin has been slayed")
                    gold = gold + random.randint(20,35)
                    xp = xp + 30
                    print(hp, "total hp left")
                    print(xp, "total xp")
                    #level(level, xp, xpcost)
                    battle = True
                    done = True
                    event(d10, dmgtaken, gold, hp, xp)
            elif attack < gAC:
                print("miss")
                print("goblins turn")
                print("the goblin attacks")
                gattack(d20, ghit, hp, xp)
                if gattacks >= AC:
                        print("you have been hit")
                        hp = hp - gdmg
                        if hp <= 0:
                            print("you are dead, to a goblin, you suck")
                            stop()
                else:
                    print("the Goblin missed")
                    print(hp)
    else:
        event(d10, dmgtaken, gold, hp)                            
def gattack(d20, ghit, hp, xp):
    gattacks = (d20(d20) + ghit)
    return gattacks
def Orc(Ohit, Ohp, Odmg, Oattack, OAC, d20, gold, xp):
    Ohit = 5
    Odmg = random.randint(1,12)
    Oattack = d20() + Ohit
    Ohp = random.randit((24,48)+ 20)
    OAC = 12
    choice = input("you encounter an Orc, he looks at you hungrily, what do you want to do? do you want to attack? yes/no?")
    if choice == "yes":
        done = False
        while not Done:
            print("rolling d20") 
            if attack >= OAC:
                Ohp = Ohp - atkdmg
                if Ohp <= 0:
                    print("the Orc has been slayed, good job!")
                    gold = gold + random.randit(60,105)
                    xp = xp + 75
                    done = True
                    event(d10, dmgtaken, gold, hp)
            elif attack < OAC:
                print("miss")
                print("Orcs turn")
                print("the Orc attacks")
                Oattack(d20, Ohit)
                if Oattack >= AC:
                        print("you have been hit")
                        hp = hp - Odmg
                        if hp <= 0:
                            print("you are dead, atleast it was not a Goblin.")
                            exit()
                        if Oattack < AC:
                            print("the Orc missed")
    else:
        event()
def Oattack(d20, Ohit):
    d20() + Ohit
def Goblinhorde(d20, HGhit, ghit, GHhp, ghp, GHdmg, gdmg, GHattack, gattack, ghAC, gold, xp):
   # for i in range(3,5)
    #Goblin()
    GHhit = (ghit)*(random.randint(3,5)),
    GHhp = (ghp)*(random.randimt(3,5)),
    GHdmg = (gdmg)*(random.randint(2,4)),
    GHattack == d20() + (ghit) * 3,
    ghAC == 12,
    choice = input("you encounter a squad of goblins, you should probably run, but what do you want to do? do you want to attack? yes/no?")
    if choice == "yes":
        done = False
        while not Done:
            print("rolling d20")
            attack(d20, GHhit)
            if attack >= ghAC:
                GHhp = GHhp - atkdmg
                if GHhp <= 0:
                    print("the squad od goblins has been crushed, Well done!")
                    gold = gold + random.randit(100, 200)
                    xp = xp + 150
                    done = True
                    event(d10, dmgtaken)
            elif attack < ghAC:
                print("miss")
                print("the squad og goblins turn")
                print("they attacks")
                GHattack(d20, GHhit)
                if GHattack >= AC:
                        print("you have been hit")
                        hp = hp - Odmg
                        if hp <= 0:
                            print("you are dead, I tolf you to run you know.")
                            exit()
                        if GHattack < AC:
                            print("the goblin squads attack missed, nice")
    else:
        event()
def GHattack(d20, GHhit):
    d20() + GHhit
def Orcsquad(Ohit, Ohp, Odmg, Oattack, OAC, d20, OShit, OShp, OSdmg, OSattack, osAC, gold, xp):
   # for i in range(3,5)
   #Orc()
    OShit = (Ohit)*(random.randint(2,4))
    OShp = (Ohp)*(random.randint(3,5))
    OSdmg = (Odmg)*(random.randint(3,5))
    OSattack = (Oattack)*(random.randint(3,5))
    osAC = 16
    choice = input("you encounter an Orc squad, good f#cking luck! well, if you have a death wish, what do you want to do? do you want to attack? yes/no?")
    if choice == "yes":
        done = False
        while not Done:
            print("rolling d20") 
            if attack >= osAC:
                OShp = OShp - atkdmg
                if OShp <= 0:
                    print("the Orc squad has been annihilated! Amazing work! you did the impossible and survived")
                    gold = gold + random.randit(300,525)
                    xp = xp + 225
                    done = True
                    event(d10, dmgtaken)
            elif attack < osAC:
                print("miss")
                print("Orc squad turn")
                print("the Orcs attacks")
                OSattack(d20, OShit)
                if OSattack >= AC:
                        print("you have been hit")
                        hp = hp - OSdmg
                        if hp <= 0:
                            print("you are dead, I f#ucking told you, dumb#ss, you were still useful you know.")
                            exit()
                        if OSattack < AC:
                            print("the Orcs missed nice!")
def OSattack(d20, OShit):
    d20() + OShit
    def Wyrm():
        Whp = 250
        Whit = 10
        Wdmg = random.randint(24,36)
        Wattack = random.randint(1, 20) + Whit
        WAC = 20
        choice = input("you encounter an Orc squad, good f#cking luck! well, if you have a death wish, what do you want to do? do you want to attack? yes/no?")
        if choice == "yes":
            battle = False
            while not Done:
                print("rolling d20") 
                if attack >= WAC:
                    Whp = Whp - atkdmg
                    if Whp <= 0:
                        print("you beat the wyrm, CONGRATS, you have done the impossible, and you have beaten the game")
                        exit()
                        
                elif attack < WAC:
                    print("miss")
                    print("Orc squad turn")
                    print("the Orcs attacks")
                    Wattack(d20, Whit)
                    if Wattack >= AC:
                        print("you have been hit")
                        hp = hp - Wdmg
                        if hp <= 0:
                            print("you are dead, no big surprise")
                            exit()
                        if Wattack < AC:
                            print("the wyrm missed thats really good!")
def Wattack(d20, Whit):
    d20() + Whit
def spawn(pmonsters, hp, xp):
    for i in range(1):
        #mon = random.choice(pmonsters)
        mon = "Goblin"
        if mon == "Goblin":
            print("goblin")
            Goblin(ghit, ghp, gdmg, gattack, gAC, d20, gold, xp, hp, attack, AC)
            print("goblin")
            print(hp)
        elif mon == "Orc" and level > 3:
            Orc(ghit, ghp, gdmg, gattack, gAC, d20, gold, xp)
            print("orc")
        elif level <= 3:
            Goblin(ghit, ghp, gdmg, gattack, gAC, d20, gold, xp, hp, attack, AC)
            print("goblin")
        elif mon == "goblinhorde" and level >= 5:
            Goblinhorde(d20, GHhit, ghit, GHhp, ghp, GHdmg, gdmg, GHattack, gattack, ghAC, gold, xp)
            print("goblinhorde")
        elif level < 5 and level >= 3:
            Orc(ghit, ghp, gdmg, gattack, gAC, d20, gold, xp)
        elif level < 3:
            Goblin(ghit, ghp, gdmg, gattack, gAC, d20, gold, xp, hp, attack, AC)
            print("goblin")
        elif mon == "Orcsquad" and level >= 7:
            Orcsquad(Ohit, Ohp, Odmg, Oattack, OAC, d20, OShit, OShp, OSdmg, OSattack, osAC, gold, xp)
            print("orcsquad")
        elif level < 7 and level >= 5:
            Goblinhorde(d20, GHhit, ghit, GHhp, ghp, GHdmg, gdmg, GHattack, gattack, ghAC, gold, xp)
        elif level < 5 and level >= 3:
            Orc(ghit, ghp, gdmg, gattack, gAC, d20, gold, xp)
        elif level < 3:
            Goblin(ghit, ghp, gdmg, gattack, gAC, d20, gold, xp, hp, attack, AC)    
            print("goblin")
            
def gearshop(gearchoice, atkdmg, gold, hp):
    gearchoice = input("this is a basic gear shop, you can upgrade either your sword or armor here, which would you like?")
    if gearchoice == "sword" and gold >= 50:
        atkdmg = atkdmg + 1
        gold = gold - 50
    if gearchoice == "armor" and gold >= 50:
        hp = hp + 8
        gold = gold - 50
    else:
        print("sorry, you can't afford it")
        print("you should go for a quest")
        spawn(pmonsters)
def shop(shopchoice, hp):
    shopchoice = input("would you like a health potion, yes/no?")
    if shopchoice == "yes" and hp >= hp - 16:
        print("here you go, drink up")
        hp = hp + 16
        print("have a good day")
        threepaths(spawn, event, city, hp, xp)
    else:
        print("sorry, but you currently cant get one at the moment")
        spawn(pmonsters)
def city(citychoice, hp):
    print("you have visited a nearby city, what would you like to do?")
    citychoice1 = input("would you like to buy some items? if yes, please type *items* if you dont, do you want to buy some gear, if yes, please type *shop* else, you can get some rest, note, you can only do one of these things")
    if citychoice == "items" or "*items*":
        shop(shopchoice, hp)
    elif citychoice == "shop" or "*shop*":
        gearshop(gearchoice, atkdmg, gold, hp)
    else:
        print("you go to bed for the day at am inn")
        hp = hp + 2 * level
    threepaths(spawn, event, city, hp, xp)
def tutorial():
    print("alright, since I do not know how to make a seperate screen, ill just tell you how this game works")
    time.sleep(3)
    print("this game is a basic rpg, all you do is walk a lonley path, fight monsters, and do events, and thats about it.")
    time.sleep(3)
    print("this was meant to be a test run of a game to see if I can make something even a little entertaining, oh, sorry for that tangent, back to the tutorial")
    time.sleep(3)
    print("the basics are that you will find a crossroads, and you can choose one of three things, you can either fight a monster, go to an event, or go to a city. there might be more later")
    time.sleep(3)
    print("once you pick a path, you can go through the choice you have made, with monsters, combat is automatic, you only need to give your input on if you want to attack the creature, or run. this loop continues until one of you either dies or runs away, if you win, you will recieve a currency known as gold, and xp, more on those later")
    time.sleep(3)
    print("for events, you will be told of an incident, and you can choose whether to help out, steal, or nothing at all. for cities, you spend gold here to either get better gear, rest, and heal.")
    time.sleep(3)
    print("xp is used for leveling up, leveling up increases all basic stats, though leveling up cost more every five levels.")
    time.sleep(1)
    print("and thats about it for now I guess, have fun")
    print(" ")
#threepaths()    
print("welcome to this random game, you are running this game, so I imagine you want to play it.")
choice = input("do you want a tutorial? yes / no ?")
if choice == "yes":
    tutorial()
    threepaths(spawn, event, city, hp, xp)
else:
    threepaths(spawn, event, city, hp, xp)


