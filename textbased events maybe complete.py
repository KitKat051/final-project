import random
dmgtaken = 0
d10 = 0
minechoice = 0
mine = 0
appletree = 0
apple = 0
kitten = 0

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
        if minechoice == yes:
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
                print("you heal" (hp + (5 * level)) hp)
                threepaths()
            else:
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
        
                
    
