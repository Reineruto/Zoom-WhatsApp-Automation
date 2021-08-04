import pyautogui as pyag

pyag.FAILSAFE = False

def run_chrome(link,group):
    pyag.hotkey("win","d")  
    pyag.hotkey("win","r")
    pyag.write("chrome")
    pyag.press("Enter")
    _whatsapp()
    _enter_link(link,group)

def _whatsapp():
# Automating the typing of URl and searching
    pyag.sleep(1)
    pyag.hotkey("win", "up")
    pyag.sleep(1)
    pyag.write('https://web.whatsapp.com/', interval=0.1)
    pyag.press("Enter")

def _enter_link(link,group):
    pyag.sleep(15)
    pyag.hotkey("ctrl", "alt", "/")
    pyag.write(group, interval=0.03)
    pyag.press("Enter")
    pyag.sleep(3)
    pyag.write(link, interval=0.03)
    pyag.press("Enter")
