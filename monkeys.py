import tools as t
import keyboard
import static as fd
from time import sleep
"""
IMPORTANT!
When gameplans are made, turn my coordinates into the decimal ones.
The function to turn it into decimals is just used when making gameplans.
"""
class Monkey:
    
    def __init__(self,name,xcoord,ycoord):
        self.xcoord = xcoord#xc = xcoord = x coordinate (width)
        self.ycoord = ycoord
        self.name = name#Name monkeys so its easy to search up
        self.keybind = fd.tower_keybinds[name]#gets the keybind from static.py for the monkey
        self.placed = False        
        

    def place(self):
        if self.placed is False:
            t.click(self.xcoord,self.ycoord)
            sleep(0.5)
            keyboard.press_and_release(self.keybind)
            sleep(0.2)
            t.click(self.xcoord,self.ycoord)
            sleep(0.5)
            #Use pytesseract to detect if "first is displayed"
            #in order to detect if its on the screen
            self.placed = True
        

    def upgrade(self,path,level=1):
        path = str(fd.upgradeKeybinds[path])
        t.click(self.xcoord,self.ycoord)#Clicks the monkey
        
        #keyboard.send(path)#Upgrades it
        sleep(0.2)
        #print("pressed key")
        #sleep(1.5)
        for x in range(0,level):
            keyboard.send(path)
            #print("press")
            sleep(0.6)
        t.click(self.xcoord,self.ycoord)
        sleep(0.4)

    def sell(self):
        t.click(self.xcoord,self.ycoord)
        keyboard.send("backspace")#no more monkey
        sleep(0.5)
    
    def setTarget(self,target):
        targets = {#can only be used once realistically
            "last":1,
            "close":2,
            "strong":3
        }
        for x in range(0,targets[target]):
            sleep(0.5)
            keyboard.send("tab")
        
"""sleep(2)
dart = Monkey("dart",485,558)
dart.place()    
dart.upgrade("BOTTOM",5)
dart.upgrade("BOTTOM")
dart.setTarget("last")
dart.sell()

br = Monkey("engineer",352,722)
br.place()
br.upgrade("TOP",5)
br.setTarget("close")
br.upgrade("MIDDLE",2)"""