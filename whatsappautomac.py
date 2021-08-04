import pyautogui

pyautogui.FAILSAFE = False


def run_chrome(link,group):
    # Automating the opening of a new Google chrome window
    pyautogui.hotkey("command", "space")
    pyautogui.write("chrome")
    pyautogui.press("return")

    # Automating the typing of URl and searching
    pyautogui.sleep(1)
    pyautogui.hotkey("command", "t")
    pyautogui.sleep(1)
    pyautogui.write('https://web.whatsapp.com/', interval=0.1)
    pyautogui.press("return")
    pyautogui.sleep(15)
    pyautogui.hotkey("command", "ctrl", "/")
    pyautogui.write(group, interval=0.03)
    pyautogui.press("return")
    pyautogui.write(link, interval=0.03)
    pyautogui.press("return")
