import pyautogui
import time

# Vide resources before

# time.sleep(3)
# print(pyautogui.position())

# Range will be the number of posts you want to like
for post in range(10):
    pyautogui.moveTo(333, 474)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.moveTo(913, 573)
    time.sleep(1)
    pyautogui.leftClick()
