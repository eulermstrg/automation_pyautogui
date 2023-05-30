# Importing the necessary libraries
import pyautogui as pyautogui
import time


# Spiral drawing using pyautogui

time.sleep(1)
distance = 300

while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button='left')
    distance = distance - 20
    pyautogui.dragRel(0, distance, 1, button='left')
    if distance <= 20:
        break
    pyautogui.dragRel(-distance, 0, 1, button='left')
    distance = distance - 20
    pyautogui.dragRel(0, -distance, 1, button='left')

# Time window created to assign fail-safe, \
# once the application masters control of your gadgets \
# in case of a crash, move the mouse to the upper corner \
# (close windows) as a fail-safe strategy
    time.sleep(4)
