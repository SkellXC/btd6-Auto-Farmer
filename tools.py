import pyautogui
import keyboard
from time import sleep
import win32api, win32con
from PIL import Image
import pytesseract
import re
import static as fd#fd = fixeddata
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
myconfig = r"--psm 7 --oem 3"#pytesseract config
csfi = r"--psm 11 --oem 3"#Config for checkScreenForItem
#-------------------------------------------------------------------------------------------------    
def findPos():
    r=0
    coords = []
    while keyboard.is_pressed("c") is False:
        r +=1
        if r == 1:
            print("Press 'n' to log the coordinates at any point and 'c' to exit")
        #pyautogui.displayMousePosition()
        if keyboard.is_pressed("n"):#When n is pressed it logs the coordinates in a list
            x, y = pyautogui.position()
            print(f"Position: {x,y}")
            sleep(0.5)
            coords.append((x,y))
            realToStandard(x,"x")
            realToStandard(y,"y")
            print("\n")
    for i in range(0,len(coords)):
        print(f"{coords[i]}")#Outputs the coordinates stored when "n" is presed
    
#-------------------------------------------------------------------------------------------------    

def click(x,y):
    win32api.SetCursorPos((x,y))#Sets the cursor where it needs to be clicked
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.2)#Delay needs to be there.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
#-------------------------------------------------------------------------------------------------    
def standardToReal(coordinate,axis):#Turns the decimal points into screen positions
    if coordinate > 1:
        print("Error! You seem to be converting the wrong type of coordinates.\n Check the standardToReal function")
    
    maxWidth = win32api.GetSystemMetrics(0)#Gets your current resolution
    maxHeight = win32api.GetSystemMetrics(1)
    newX = coordinate*maxWidth
    newY= coordinate*maxHeight#Gets coordinates relevant to your resolution
    #print(f"{maxWidth}x{maxHeight}\n{newX} x {newY}")
    newX = int(newX)
    newY = int(newY)
    if axis == "x":
        return newX
    elif axis == "y":
        return newY
#-------------------------------------------------------------------------------------------------    
def realToStandard(coordinate,axis):
    if coordinate < 1:
        print("Error! You seem to be converting the wrong type of coordinates.\n Check the realToStandard function")
    #axis should be either x or y in lowercase
    maxWidth = win32api.GetSystemMetrics(0)#Gets your current resolution
    maxHeight = win32api.GetSystemMetrics(1)
    newX = coordinate/maxWidth
    newY = coordinate/maxHeight
    #print(f"{maxWidth}x{maxHeight}\n{newX} x {newY}")
    if axis == "x":
        print(f"x = {newX}")
        return newX
    elif axis == "y":
        print(f"y = {newY}")
        return newY
    else:
        print("Error! Your are doing something wrong.\nFix it.\nCheck the usage of the coordinate switching function")
#------------------------------------------------------------------------------------------------- 

def checkScreenFor(item):
    #Uses config #11 on pytesseract to search for any text (takes 2-3 seconds usually) and returns it
    #It then looks for the item and returns true if it finds it or tries again in 15 seconds.
    #Could cause issues. Change how it works or use carefully
    sleep(1)
    screenshot = pyautogui.screenshot()
    #start = time.time()
    text = pytesseract.image_to_string(screenshot,config=csfi) 
    #end = time.time()
    #print(f"It took {end-start} seconds to run this")
    #print(text)
    if item in text.lower():
        #print("Item found!")
        return True

    else:
        print(f"checkScreenForItem has not found '{item}'")
        sleep(5)
#------------------------------------------------------------------------------------------------- 
def getRound():
    #Takes a screenshot and then crops it to the rounds part (so its faster) and then gets the round
    #It then removes the bit after the round (eg /80 or /100) to get the round number.
    screenshot = pyautogui.screenshot()
    round = 0
    toprx = 1726   #0.67421875
    topry = 0      #0
    width = 158
    height = 80
    roundImage = screenshot.crop((toprx,topry,toprx+width,topry+height))#gets dimensions of cropped image
    #roundImage.show()
    text = pytesseract.image_to_string(roundImage,config=myconfig)
    text =  "".join(text.split())
    text = text.lower()
    text = text.replace("round","")
    #print(text)
    if "80" in text:
        round = text.replace("/80","")
    elif "100" in text:
        round = text.replace("/100","")#Gets rid of the other info leaving just the round number
    round = re.sub(r'\D',"",round)
    if round == "147100":
        round = int(round)
        round -= 147086
    return int(round)
#------------------------------------------------------------------------------------------------- 

def enterMap(map,difficulty,gamemode):
    #standardToReal(fd.buttons["homePlayButton"][0],"x")
    click(standardToReal(fd.buttons["homePlayButton"][0],"x"),standardToReal(fd.buttons["homePlayButton"][1],"y"))
    sleep(1)
    goToMapPage(12)
    sleep(1)
    click(standardToReal(fd.mapLocations[map][0],"x"),standardToReal(fd.mapLocations[map][1],"y"))
    sleep(1)
    click(standardToReal(fd.buttons[difficulty][0],"x"),standardToReal(fd.buttons[difficulty][1],"y"))
    sleep(1)
    click(standardToReal(fd.buttons[gamemode][0],"x"),standardToReal(fd.buttons[gamemode][1],"y"))


def goToMapPage(page):
    #sleep(0.1)
    click(standardToReal(0.630078125,"x"),standardToReal(0.8981481481481481,"y"))
    sleep(1)
    click(standardToReal(0.36640625,"x"),standardToReal(0.8962962962962963,"y"))
    sleep(1)
    for x in range(0,page):
        click(standardToReal(0.7640625,"x"),standardToReal(0.39444444444444443,"y"))
        sleep(0.1)



