import pyautogui
import time
import random


# Wait for 3 seconds
time.sleep(10)
tab_x, tab_y = 110, 3
tab_end_x, tab_end_y = 231, 15
tab_save_x, tab_save_y = 670, 1045
# Get the current mouse position
current_x, current_y = pyautogui.position()

#Have to change this time to time
x, y = 1940, 578  # Example pixel coordinates
X_Paste, Y_Paste = 2286, 566
i=0
while i<5:
    pyautogui.moveTo(tab_x, tab_y)
    pyautogui.click(tab_x, tab_y)
    time.sleep(3)
    pyautogui.moveTo(tab_save_x, tab_save_y)
    pyautogui.click(tab_save_x, tab_save_y)
    time.sleep(3)
    pyautogui.moveTo(tab_end_x, tab_end_y)
    pyautogui.click(tab_end_x, tab_end_y)
    time.sleep(3)
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
    pyautogui.press('pagedown')
    pyautogui.click(x, y)
    pyautogui.click(x, y)
    pyautogui.click(x, y)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(X_Paste, Y_Paste)
    pyautogui.hotkey('ctrl', 'v')
    y=y+32
    Y_Paste=Y_Paste+25
    i=i+1
    time.sleep(random.randint(250, 300))
# # pyautogui.moveTo(x, y)

print(f"Current mouse position: X={current_x}, Y={current_y}")
