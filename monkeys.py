import tools as t
import keyboard
import static as fd
from time import sleep
from typing import Literal

class Monkey:
    
    def __init__(self,monkeyType,xcoord,ycoord):
        self.xcoord = xcoord#xc = xcoord = x coordinate (width)
        self.ycoord = ycoord
        self.monkeyType = monkeyType# Identifies the monkey to get its keybind
        self.keybind = fd.tower_keybinds[monkeyType]# Fetches the keybind from static.py
        self.placed = False        
        

    def place(self):
        if self.placed is False:
            t.click(self.xcoord,self.ycoord)
            sleep(0.5)
            keyboard.press_and_release(self.keybind)
            sleep(0.2)
            t.click(self.xcoord,self.ycoord)
            sleep(0.5)
            self.placed = True
        

    def upgrade(self,path : Literal['TOP', 'MIDDLE', 'BOTTOM'], level=1):
        path = path.upper()
        path = str(fd.upgradeKeybinds[path])
        t.click(self.xcoord,self.ycoord)#Clicks the monkey
        
        sleep(0.2)
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
    
    def setTarget(self,target : Literal['last', 'close', 'strong']):
        targets = {
            # Only adjustable once.
            "last":1,
            "close":2,
            "strong":3
        }
        target = target.lower()
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