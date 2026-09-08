import keyboard
import pyautogui
from time import sleep

def getPosition():
    coords = []
    print("Press 'n' to log the coordinates.\nPress 'c' to exit")
    while not keyboard.is_pressed("c"):
        
        
        if keyboard.is_pressed("n"):
            x,y = pyautogui.position()
            print(f"({x},{y})")
            sleep(0.5)
            coords.append((x,y))
            print("Press 'n' to log another set of coordinates.\nPress 'c' to exit")

    for x in range(0,len(coords)):
        print(f"Position {x+1}: {coords[x]}")
    print("Exited program")

if __name__ == "__main__":
    getPosition()