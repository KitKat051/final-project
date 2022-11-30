#player stats
import random
def d6():
    random.randint(1,6)
HP = (8 * level)
atkdmg = d6() + (level // 2)
AC = 12 + (level // 5)
dmgtaken = 0
d10 = 0
minechoice = 0
mine = 0
appletree = 0
apple = 0
kitten = 0
#goblin stats
ghit = 0
ghp = 0
gdmg = 0
gattack = 0
gAC = 10
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

yes = "yes"
no = "no"


level = 0
XP = (0)
xpcost = (1)
monsters = ['Goblin', 'Orc', 'Goblin-horde', 'Orcsquad',]
pmonsters = ['Goblin', 'Orc', 'Goblin-horde', 'Orcsquad']
bmonster = ['wyrm']
spawn_monster = random.randit(1,1)

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
def event(d10, dmgtaken, d10, minechoice, mine, appletree, apple, kitten ):
    d10 = random.randint(1,5)
    if d10 == 1:
        print("it's a trap!")
        print("you have steped in a punji trap")
        dmgtaken = random.randint(4,12)
        print("you have taken", dmgtaken, "damage")
        hp = hp - dmgtaken
        if hp <= 0:
            print("you have died to a hunting trap, atleast it was not a goblin")
        else:
            threepaths()
    if d10 == 2:
        print("you have found a wandering monster")
        spawn()
    if d10 == 3:
        print("you have found an abandonded mine, what do you want to do")
        minechoice = input("do you want to explore it? yes/no")
        if minechoice == "yes":
            mine = random.randint(1,2)
            if mine == 1:
                print("you have struck gold")
                gold = gold + 100
                threepaths()
            if mine == 2:
                print("you have found nothing, not surprising")
                threepaths()
        else:
            print("you have decided to leave the mine, no use in wasting time")
            threepaths()
    if d10 == 4:
        appletree = input("you see an orchard, do you want to have a look around no one else is here? yes/no")
        if appletree == yes:
            apple = input("you can either eat the apples now or sell them later, do you want to eat them now? yes/no")
            if apple == yes:
                hp = hp + (5 * level)
                print("the apple taste like an apple, your welcome")
                print("you heal", (hp + (5 * level)),
                threepaths()
            if apple == "no":
                print("you sell the apple")
                gold = gold + 30
                print("you get 30 gold")
                threepaths()
        else:
            print("you leave the orchard without taking anything, what a good guy you are.")
            threepaths()
    if d10 == 5:
        kitten = input("you see a kitten on the side of the road, he is meowing at you, do you want to pet it? yes/no")
        if kitten == yes:
            print("you pet the kitten")
            threepaths()
        else:
            print("you do not pet the kitten")
            threepaths()
def level(level, XP, xpcost):
    if level >= 4:
        xpcost = 1
        level = (XP / (100 * xpcost))
        xp = xp - (100 * xpcost)
    if level <= 5 and level >= 9:
        xpcost = 2
        level = (XP / (100 * xpcost))
        xp = xp - (100 * xpcost)
    if level <= 10 and level >= 15:
        xpcost = 3
        level = (XP / (100 * xpcost))
    if level <= 16 and level >= 19:
        xpcost = 4
        level = (XP / (100 * xpcost))
        xp = xp - (100 * xpcost)
    if level == 20:
        xpcost = 100000
        level = (XP / (100 * xpcost))
        xp = xp - (100 * xpcost)

def d20():
    random.randint(1,20)
def spawn(pmosters):
    if level >= 20:
        for i in range(bmonster):
            if bmonster = 'wyrm':
                wyrm()
    else:
        for i in range((pmonsters) - random.randint(1,2)):
            pmonster = random.choice(pmonsters)
            print(pmonster)
            if monsters == "Goblin":
                Goblin(ghit, ghp, gdmg, gattack, gAC, d20) 
            if monster == "Orc" and level > 3:
                Orc(ohit, ghp, gdmg, gattack, gAC, d20)
            elif level <= 3:
                Goblin(ghit, ghp, gdmg, gattack, gAC, d20)
            if pmonster == "goblinhorde" and level >= 5:
                Goblinsquad(d20, HGhit, ghit, GHhp, ghp, GHdmg, gdmg, GHattack, gattack, ghAC)
            elif level < 5 and level >= 3:
                Orc()
            elif level < 3:
                Goblin(ghit, ghp, gdmg, gattack, gAC, d20)
            if pmonster == "Orcsquad" and level >= 7:
                Orcsquad(Ohit, Ohp, Odmg, Oattack, OAC, d20, OShit, OShp, OSdmg, OSattack, osAC)
            elif level < 7 and level >= 5:
                Goblinhorde()
            elif level < 5 and level >= 3:
                Orc()
            elif level < 3:
                Goblin(ghit, ghp, gdmg, gattack, gAC, d20) 
        #if pmonster == "Orcsquad" and level >= 7:
         #   Orcsquad()
        #elif pmonster == "goblinhorde" and level >= 5 and level < 7
         #   Goblinsquad(d20, HGhit, ghit, GHhp, ghp, GHdmg, gdmg, GHattack, gattack, ghAC)
            
            
def Goblin(ghit, ghp, gdmg, gattack, gAC, d20):
    ghit = 2
    ghp = random.randit((6,12) + 10)
    gdmg = random.randit(1,6)
    gatttack = d20() + ghit
    gAC = 10
    choice = input("you encounter a Goblin, what do you want to do? do you want to attack? yes/no?")
    if choice == "yes":
        done = False
        while not Done:
            print("rolling d20")
            d20()
            if attack >= gAC:
                ghp = ghp - atkdmg
                if ghp <= 0:
                    print("the Goblin has been slayed")
                    gold = gold + random.randit(20,35)
                    xp = xp + 30
                    level()
                    done = True
            elif attack < gAC:
                print("miss")
                print("goblins turn")
                print("the goblin attacks")
                gattack(d20, ghit)
                if gattack >= AC:
                        print("you have been hit")
                        hp = hp - gdmg
                        if hp <= 0:
                            print("you are dead, to a goblin, you suck")
                            exit()
                        if gattack < AC:
                            print("the Goblin missed")
    else:
        event()
    event()        
def gattack(d20, ghit):
    d20() + ghit
def Orc(Ohit, Ohp, Odmg, Oattack, OAC, d20):
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
                    level()
                    done = True
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
    event()        
def Oattack(d20, Ohit):
    d20() + Ohit
def Goblinsquad(d20, HGhit, ghit, GHhp, ghp, GHdmg, gdmg, GHattack, gattack, ghAC):
   # for i in range(3,5)
    #Goblin()
    GHhit == (ghit)*(random.randint(3,5),
    GHhp == (ghp)*(random.randimt(3,5),
    GHdmg == (gdmg)*(random.randint(2,4),
    GHattack == d20() + (ghit) * 3,
    ghAC == 12,
    choice == input("you encounter a squad of goblins, you should probably run, but what do you want to do? do you want to attack? yes/no?")
    if choice == "yes":
        done = False
        while not Done:
            print("rolling d20")
            attack(d20, phit)
            if attack >= ghAC:
                GHhp = GHhp - atkdmg
                if GHhp <= 0:
                    print("the squad od goblins has been crushed, Well done!")
                    gold = gold + random.randit(100, 200)
                    xp = xp + 150
                    level()
                    done = True
                else:
                    GHattack(d20, GHhit)
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
                elif GHattack < AC:
                            print("the goblin squads attack missed, nice")
    else:
        event()
    event()        
def GHattack(d20, GHhit):
    d20() + GHhit
def Orcsquad(Ohit, Ohp, Odmg, Oattack, OAC, d20, OShit, OShp, OSdmg, OSattack, osAC):
   # for i in range(3,5)
   #Orc()
    OShit = (Ohit)*(random.randint(2,4)
    OShp = (Ohp)*(random.randint(3,5)
    OSdmg = (Odmg)*(random.randint(3,5)
    OSattack = (Oattack)*(random.randint(3,5)
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
                    level()
                    done = True
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
    else:
        event()
    event()        
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
            done = False
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
    gearchoice = 0
shopchoice = 0
citychoice = 0
def gearshop(gearchoice, dmg, gold, hp):
    gearchoice = input("this is a basic gear shop, you can upgrade either your sword or armor here, which would you like?")
    if gearchoice = "sword" and gold >= 50:
        dmg = dmg + 1
        gold = gold - 50
    if gearchoice = "armor" and gold >= 50:
        hp = hp + 8
        gold = gold - 50
    else:
        print("sorry, you can't afford it")
        print("you should go for a quest")
        spawn(pmonster)
def shop(shopchoice, hp):
    shopchoice = input("would you like a health potion, yes/no?")
    if shopchoice = "yes" and hp >= hp - 16:
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
    if citychoice = "items" or "*items*":
        shop()
    if citychoice = "shop" or "*shop*":
        gearshop()
    else:
        print("you go to bed for the day at am inn")
        hp = hp + 2 * level
    threepaths()



