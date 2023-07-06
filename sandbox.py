import tools as t
from time import sleep
import time
import static as fd
import keyboard
import pytesseract
import pyautogui
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"#You need to replace this with the filepath to tesseract.exe
myconfig = r"--psm 11 --oem 3"
"""
https://muthu.co/all-tesseract-ocr-options/
Use it to find the ones you feel are right but in general
11 is fine for searching the whole screen and 7 is for 
checking what round the game is on.
"""
