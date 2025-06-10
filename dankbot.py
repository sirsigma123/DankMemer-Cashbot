import webbrowser
import pyautogui as py
import time 


webbrowser.open('https://discord.com/channels/1380143490045972500/1380143490654015611')

time.sleep(5)  # Wait for the page to load
i=0

while True:
    py.write('/dig')
    time.sleep(2)  # Wait for the command to be typed
    py.press('enter')
    py.press('enter')
    time.sleep(8)
    py.write('/hunt')

    time.sleep(2)  # Wait for the command to be typed
    py.press('enter')
    py.press('enter')
    time.sleep(8)
    i+=1
    print(str(i) + 'rounds have been completed')