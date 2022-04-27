from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

time.sleep(5)

while keyboard.is_pressed('q') == False:

    if pyautogui.locateOnScreen('leftarrow.png', region=(1010, 50, 650, 200), grayscale=False, confidence=0.7) != None:
        pyautogui.keyDown('left')
        time.sleep(0.1)
        pyautogui.keyUp('left')

    if pyautogui.locateOnScreen('rightarrow.png', region=(1010, 50, 650, 200), grayscale=False, confidence=0.7) != None:
        pyautogui.keyDown('right')
        time.sleep(0.1)
        pyautogui.keyUp('right')

    if pyautogui.locateOnScreen('uparrow.png', region=(1010, 50, 650, 200), grayscale=False, confidence=0.7) != None:
        pyautogui.keyDown('up')
        time.sleep(0.1)
        pyautogui.keyUp('up')

    if pyautogui.locateOnScreen('downarrow.png', region=(1010, 50, 650, 200), grayscale=False, confidence=0.7) != None:
        pyautogui.keyDown('down')
        time.sleep(0.1)
        pyautogui.keyUp('down')