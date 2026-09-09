import pyautogui
import keyboard
import numpy as np
from time import sleep
import win32api, win32con
import re
import src.static as fd#fd = fixeddata
from typing import Literal


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.2)# Do not adjust
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def isOnHomeScreen() -> bool:
    try:
        pyautogui.locateOnScreen(r'images/home_play_button.PNG', confidence=0.8)
        return True
    except:
        return False


def enterMap(page: int, map: str, difficulty: str , gamemode: str):
    click((fd.map_navigation_buttons["HOME_PLAY_BUTTON"][0]),
          (fd.map_navigation_buttons["HOME_PLAY_BUTTON"][1]))
    sleep(1)
    _goToMapPage(page)
    sleep(1)
    click(fd.map_locations[map][0],
          fd.map_locations[map][1])
    sleep(1)
    click((fd.choose_gamemode_buttons[difficulty][0]),
          (fd.choose_gamemode_buttons[difficulty][1]))
    sleep(1)
    click((fd.choose_gamemode_buttons[gamemode][0]),
          (fd.choose_gamemode_buttons[gamemode][1]))
    print("Waiting for map to load.")
    sleep(8)
    print("Map has been loaded")
    keyboard.send("enter")


def _goToMapPage(page):
    expert = fd.map_navigation_buttons["EXPERT_BUTTON"]
    beginner = fd.map_navigation_buttons["BEGINNER_BUTTON"]
    rightArrow = fd.map_navigation_buttons["RIGHT_ARROW"]
    sleep(0.1)
    click(expert[0], expert[1])
    sleep(1)
    click(beginner[0], beginner[1])
    sleep(1)
    for x in range(0,page-1):
        click(rightArrow[0], rightArrow[1])
        sleep(0.1)



def correctRound(correctRound: int, previousRound: int, intendedRound: int):
    if correctRound == intendedRound:
        if correctRound == previousRound:
            return False
        else:
            return True
    # The program will attempt to place the towers on every cycle, regardless
    # of whether it has already been placed. This is designed to keep track of
    # whether the towers have been placed on the current round.

def checkGameEnd() -> str:
    try:
        gameWon = pyautogui.locateOnScreen(r'images/next.PNG', confidence=0.8)
        if gameWon:
            return 'win'

    except pyautogui.ImageNotFoundException:
        try:
            homeButtonIsVisible = pyautogui.locateOnScreen(r'images/endHomeButton.PNG',
                                                        confidence=0.8)
            if homeButtonIsVisible:
                return 'loss'
        except pyautogui.ImageNotFoundException:
            return None


def endGame(state: Literal['win','loss']) -> bool:
    state = state.lower()

    if state == 'win':
        _gameWonSequence()
        return True

    elif state == 'loss':
        _gameLostSequence()
        return True
    else:
        return False

def _gameWonSequence():
    click(955,909)# Click 'next'
    sleep(3)
    click(719, 849)# Click 'home'
    sleep(5)
    print("Back at home screen")

def _gameLostSequence():
    click(719, 849)# Click 'home' on the loss page
    sleep(5)
    print("Back at home screen (loss)")
