import tools as t
from time import sleep
import time
import static as fd
import keyboard
import pytesseract
import pyautogui
import cv2
import re
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
myconfig = r"--psm 11 --oem 3"
'''sleep(1)
screenshot = pyautogui.screenshot()
#image = t.getRound(screenshot)
#image.show()
#start = time.time()
screenshot.show()
text = pytesseract.image_to_string(screenshot,config=myconfig) 


print(text)'''
#screenshot = pyautogui.screenshot()
#print(t.checkScreenFor("heroes"))

#t.enterMap("darkCastle","HARD_MODE","STANDARD_GAME_MODE")
targets = {#can only be used once realistically
    "last":1,
    "close":2,
    "strong":3

}
print(targets["close"])