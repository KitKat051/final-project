import random
import time
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

HP = (12 * level)
level = (XP / 100)
XP = (0)
xpcost = (1)
monsters = ['Goblin', 'Orc', 'Goblin-horde', 'Orcsquad', 'mysterious-portal']
pmonsters = ['Goblin', 'Orc', 'Goblin-horde', 'Orcsquad']
spawn-monster == random.randit(1,1)
def level(level, XP, xpcost):
    if level >= 4:
        xpcost = 1
        level = (XP / (100 * xpcost))
    if level <= 5 and level >= 9:
        xpcost = 2
        level = (XP / (100 * xpcost))
    if level <= 10 and level >= 15:
        xpcost = 3
        level = (XP / (100 * xpcost))
    if level <= 16 and level >= 19:
        xpcost = 4
        level = (XP / (100 * xpcost))
    if level == 20:
        xpcost = 100000
        level = (XP / (100 * xpcost))

def d20():
    random.randint(1,20)
def spawn(pmosters):
    for i in range(spawn-monster):
        print(i,end = random.choice(pmonsters))
        if monsters == "Goblin":
            Goblin(ghit, ghp, gdmg, gattack, gAC, d20) 
        if monster == "Orc" and level > 3:
            Orc(ghit, ghp, gdmg, gattack, gAC, d20)
        elif level <= 3:
            Goblin()
        if pmonster == "goblinhorde" and level >= 5:
            Goblinsquad(d20, HGhit, ghit, GHhp, ghp, GHdmg, gdmg, GHattack, gattack, ghAC)
        elif level < 5 and level >= 3:
            Orc()
        elif level < 3:
            Goblin()
        if pmonster == "Orcsquad" and level >= 7:
            Orcsquad()
        elif level < 7 and level >= 5:
            Goblinhorde()
        elif level < 5 and level >= 3:
            Orc()
        elif level < 3:
            Goblin()    
            
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
            if attack >= gAC:
                ghp = ghp - atkdmg
                if ghp <= 0:
                    print("the Goblin has been slayed")
                    gold = gold + random.randit(20,35)
                    xp = xp + 30
                    done = True
                    event()
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
                            stop()
                        if gattack < AC:
                            print("the Goblin missed")
    else:
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
                    done = True
                    event()
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
                            stop()
                        if Oattack < AC:
                            print("the Orc missed")
    else:
        event()
def Oattack(d20, Ohit):
    d20() + Ohit
def Goblinsquad(d20, HGhit, ghit, GHhp, ghp, GHdmg, gdmg, GHattack, gattack, ghAC):
   # for i in range(3,5)
    #Goblin()
    GHhit = (ghit)*(random.randint(3,5),
    GHhp = (ghp)*(random.randimt(3,5),
    GHdmg = (gdmg)*(random.randint(2,4),
    GHattack == d20() + (ghit) * 3,
    ghAC == 12,
    choice = input("you encounter a squad of goblins, you should probably run, but what do you want to do? do you want to attack? yes/no?")
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
                    done = True
                    event()
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
                            stop()
                        if GHattack < AC:
                            print("the goblin squads attack missed, nice")
    else:
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
                    done = True
                    event()
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
                            stop()
                        if OSattack < AC:
                            print("the Orcs missed nice!")
def OSattack(d20, OShit):
    d20() + OShit
def MysterousPortal():
    php = 250
    pturn = 17
    for i in range(spawn-monster):
        print(i,end = random.choice(pmonsters))
