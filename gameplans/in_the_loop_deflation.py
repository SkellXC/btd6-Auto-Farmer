import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tools as t
from templateMatcher import getRoundNumber
from time import sleep
import monkeys
import keyboard

"""homepage = False
while not t.isOnHomeScreen() and not keyboard.is_pressed("c") :
    print("Error! You're not on the homescreen.")
    print("Trying again in 1s")
    print("Hold 'C' to cancel")
    sleep(1)

print("Home screen detected. Starting the macro.")
homepage = True

gameRunning = True
sleep(1)
t.enterMap(1, "MAP_INDEX_2","EASY", "DEFLATION")
"""
gameRunning = True
gameStarted = False
previousRound = 0
sleep(2)


sniper1 = monkeys.Monkey("sniper", 1225, 889)
alchemist1 = monkeys.Monkey("alchemist", 1325, 770)
village1 = monkeys.Monkey("village", 1325, 867)
bomb1 = monkeys.Monkey("bomb", 1133, 725)

while gameRunning:
    sleep(0.5)
    currentRound = getRoundNumber(60)
    sameRound = (currentRound == previousRound)
    gameEnded = t.handleGameEnd()
    
        

    if currentRound == -1:
        print("Error! Ending macro.\nPlease restart.")
        break
    elif t.correctRound(currentRound,previousRound, 31):
        sniper1.place()
        sniper1.upgrade("BOTTOM", 4)
        sniper1.upgrade("MIDDLE", 2)
        village1.place()
        village1.upgrade("TOP", 3)
        village1.upgrade("MIDDLE", 2)
        alchemist1.place()
        alchemist1.upgrade("TOP", 4)
        alchemist1.upgrade("BOTTOM")
        bomb1.place()
        bomb1.upgrade("TOP",2)
        bomb1.upgrade("BOTTOM",3)
        if not gameStarted:
            gameStarted = True
            keyboard.send("space")
            sleep(0.4)
            keyboard.send("space")


    previousRound = currentRound