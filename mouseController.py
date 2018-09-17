import pyautogui, sys

def click():
    pyautogui.click()
def right():
    pyautogui.moveRel(50, None)
def left():
    pyautogui.moveRel(-50, None)
def up():
    pyautogui.moveRel(None, -50)
def down():
    pyautogui.moveRel(None, 50)
