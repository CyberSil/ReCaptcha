import pyautogui

import pyautogui as auto

x, y = auto.locateCenterOnScreen('bib.png', grayscale=True)
print(x, y)
pyautogui.click(x - 100,y,button='left')
pyautogui.click(x-55,y,button='left')
#pyautogui.PAUSE = 2.5
#pyautogui.tripleClick()
