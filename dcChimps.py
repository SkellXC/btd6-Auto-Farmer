I '''
This file just handles what monkeys are placed, where they are placed and at
what rounds as well as what map it should be on.
!!If you want to go to the last page, its 12 clicks, not 13 (since your on the first page already)
If you want to make your own heres the format:





'''
import tools as t
import monkeys
from time import sleep
import static as fd
import keyboard
import pytesseract
import pyautogui


homepage = False
while a:
    if t.checkScreenFor("heroes"):# Checks if your on the homepage
        homepage = False
    else:
        sleep(1)
        keyboard.send("esc")
#t.enterMap("darkCastle","HARD_MODE","UWCHIMPS_MODE")#Enters the game
#sleep(6)#To load into the game
def correctRound(cr,pr,intendedRound):
    if cr == intendedRound:
        if cr == pr:# cr = current round
            return False# pr = previous round
        else:
            return True
    # This is here because when the round starts, it places everything however since
    # it checks at fixed intervals, it ends up redoing the same thing until the round
    # changes. This function stops that. Idk if theres a better way to do it.

# Create the monkeys that will be placed beforehand


dart1 = monkeys.Monkey("dart",0.35234375,0.45740740740740743)#topMid
waterBottom = monkeys.Monkey("submarine",0.549609375,0.6398148148148148)
sub0 = monkeys.Monkey("submarine",0.55,0.4009259259259259)
dart0 = monkeys.Monkey("dart",0.521484375,0.6166666666666667)

previousRound = 0


hero = monkeys.Monkey("hero",0.469921875,0.41203703703703703)
spike = monkeys.Monkey("spike",0.719921875,0.5083333333333333)
druid1 = monkeys.Monkey("druid",0.503515625,0.40925925925925927)#Right of obyn
druid2= monkeys.Monkey("druid",0.43828125,0.4111111111111111)
start = False
#dart1.place()
while 1:
    currentRound = t.getRound()
    if correctRound(currentRound,previousRound,6):
        dart0.place()
        sub0.place()
    if start is False:
        keyboard.send("space")
        sleep(0.5)
        keyboard.send("space")
        start = True
    if correctRound(currentRound,previousRound,7):
        dart1.place()
        
    if correctRound(currentRound,previousRound,10):
        sub0.upgrade("bottom",1)
    if correctRound(currentRound,previousRound,13):
        hero.place()
    if correctRound(currentRound,previousRound,14):
        sub0.upgrade("top",1)
        # its detected as 147100 so correctRound subtracts in order to get 14
        # because idk how to fix the image rec (#1)
    if correctRound(currentRound,previousRound,15):
        sleep(5)
        sub0.upgrade("top",1)
    if correctRound(currentRound,previousRound,19):
        sleep(3)
        spike.place()
    if correctRound(currentRound,previousRound,22):
        spike.upgrade("bottom",2)
        sleep(0.5)
        spike.setTarget("strong")
    if correctRound(currentRound,previousRound,23):
        druid1.place()
    if correctRound(currentRound,previousRound,24) or correctRound(currentRound,previousRound,247):
        # Idk how to fix the image rec (#2) so this is the easiest solution
         druid1.upgrade("bottom",1)
    if correctRound(currentRound,previousRound,26):
        druid1.upgrade("middle",1)
    if correctRound(currentRound,previousRound,29):
        sub0.upgrade("bottom",1)
    if correctRound(currentRound,previousRound,29):
        sleep(4)
        druid1.upgrade("bottom",1) 
    if correctRound(currentRound,previousRound,30):
        druid2.place()
    if correctRound(currentRound,previousRound,32):
        druid2.upgrade("bottom",2)
        druid2.upgrade("middle",1)  
    if correctRound(currentRound,previousRound,34):
        sleep(4)
        spike.upgrade("top",2)
    previousRound = currentRound 


"""
You get the gist of it.
I'd recommend finding a youtube tutorial and making your own gameplan, ideally with the 
least amount of towers

"""
