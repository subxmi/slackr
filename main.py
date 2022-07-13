import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetingid, pswd):
    #Opens up the zoom app
    subprocess.call("C:/Users/Subxmi/AppData/Roaming/Zoom/bin/Zoom.exe")

    time.sleep(5)

    #click the join button
    join_btn = pyautogui.locateCenterOnScreen('join_button.PNG')
    pyautogui.move(join_btn)
    pyautogui.click()
sign_in('6109684015', '8AmcpK')
