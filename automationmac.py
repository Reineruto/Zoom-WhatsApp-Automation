import pyautogui as pyag

pyag.FAILSAFE = False

def run_chrome(link):
    pyag.hotkey("command", "space")
    pyag.write("chrome")
    pyag.press("return")
    pyag.sleep(1)
    pyag.hotkey("command", "t")
    pyag.sleep(1)
    _search_url(link)
    _open_meet()

def _search_url(link):
    pyag.sleep(5)
    pyag.write(link, interval=0.03)
    pyag.press("return")

def _open_meet():
    pyag.sleep(5)
    pyag.press("return")

