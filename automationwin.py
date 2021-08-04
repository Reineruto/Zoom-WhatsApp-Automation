import pyautogui as pyag

pyag.FAILSAFE = False

def run_chrome(link):
    pyag.hotkey("win","d") 
    pyag.hotkey("win","r")
    pyag.write("chrome")
    pyag.press("Enter")
    _search_url(link)
    _open_meet()

def _search_url(link):
    pyag.sleep(5)
    pyag.hotkey("win","up")
    pyag.sleep(1)
    pyag.write(link,interval=0.03)
    pyag.press("Enter")

def _open_meet():
    pyag.sleep(5)
    pyag.press("left")
    pyag.press("enter")