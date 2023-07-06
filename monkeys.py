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
        if self.xcoord < 1:
            self.xcoord = t.standardToReal(self.xcoord,"x")
        if self.ycoord < 1:
            self.ycoord = t.standardToReal(self.ycoord,"y")
        
        

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
        

    def upgrade(self,path,level):
        path = str(fd.upgradeKeybinds[path])
        t.click(self.xcoord,self.ycoord)#Clicks the monkey
        
        
        #keyboard.send(path)#Upgrades it
        sleep(0.1)
        
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
#sleep(2)
#dart = Monkey("dart",0.45,0.8546296296296296)
#dart.place()    
#dart.upgrade("bottom",5)
#dart.upgrade("bottom")

#br = Monkey("engineer",0.45,0.8546296296296296)
#br.place()
#br.upgrade("top",5)
#br.upgrade("middle",2)