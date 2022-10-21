import pyautogui, pyperclip, time
import time
import cv2
from time import sleep
import sys
import tkinter
line_1 = "  Vừa nhấn vô đây đúng khumm=))\n\n"
line_2 = "  Quay trờ lại đoạn chat với anh gòi đợi 5s bất ngờ sẽ đến với em:D\n\n"

for l1 in line_1:
    print(l1, end='')
    sys.stdout.flush()
    sleep(0.06)
for l2 in line_2:
    print(l2, end='')
    sys.stdout.flush()
    sleep(0.06)
sleep(2)
msg = "Em iu Anh❤!"
for i in range(5,0,-1):
    print(i ,"...",end=" ",flush=True)
    time.sleep(1)
pyperclip.copy(msg)
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")