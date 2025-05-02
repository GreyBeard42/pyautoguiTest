import pyautogui
import cv2
import numpy as np
import time

w, h = pyautogui.size()
x, y = pyautogui.position()

def findImage(path):
    template = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

    mx = cv2.minMaxLoc(result)[3][0]
    my = cv2.minMaxLoc(result)[3][1]
    return mx, my, cv2.minMaxLoc(result)[0]

openchrome = findImage(r"C:\Users\greys\OneDrive\Desktop\code\pyautoguiTest\chrome.png")
pyautogui.moveTo(openchrome[0], openchrome[1])
pyautogui.click()
pyautogui.moveTo(openchrome[0], openchrome[1]-75)
pyautogui.click()
print("chrome should be open")

pyautogui.hotkey('ctrl', 't')
print("opened new tab")

pyautogui.typewrite(['y','o','u','t','u','b','e','.','c','o','m','ENTER'], interval=0)
print("opened youtube")

time.sleep(1)

waiting = True
while waiting:
    searchbar = findImage(r"C:\Users\greys\OneDrive\Desktop\code\pyautoguiTest\ytsearch.png")
    pyautogui.moveTo(searchbar[0], searchbar[1])
    if searchbar[1] < h/2:
        waiting = False
    time.sleep(0.5)
print("youtube loaded")

time.sleep(2)
searchbar = findImage(r"C:\Users\greys\OneDrive\Desktop\code\pyautoguiTest\ytsearch.png")

pyautogui.moveTo(searchbar[0]+100, searchbar[1]+30)
pyautogui.click()
time.sleep(0.1)
pyautogui.typewrite("lofi live", interval=0.1)
pyautogui.hotkey("ENTER")
print("searched for lofi")

time.sleep(1)

pyautogui.moveTo(w-10, searchbar[1]+30)
waiting = True
while waiting:
    pyautogui.scroll(-500)
    live = findImage(r"C:\Users\greys\OneDrive\Desktop\code\pyautoguiTest\live.png")
    if live[0] > 800 and live[1] > 300:
        pyautogui.moveTo(live[0]-100, live[1])
        waiting = False
        pyautogui.click()
print("found lofi stream")
pyautogui.moveTo(0, 0)
