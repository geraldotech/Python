import pyautogui
import pyperclip
import time

time.sleep(2)
# await pages loading time
pyautogui.PAUSE = 1.5

# abrir uma nova aba no navegador - CTRL + t
pyautogui.hotkey('ctrl', 't')
pyperclip.copy("https://retaguarda.xbyteautomacao.com.br/Conta/Login?ReturnUrl=%2f")
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey("enter")

# scrol click
pyautogui.click(x=1431, y=795)

# login
pyautogui.click(x=676, y=574)
pyperclip.copy("geraldo.filho92@hotmail.com")
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')
pyperclip.copy("@rpa8536")
pyautogui.hotkey('end')
pyautogui.hotkey('ctrl', 'v')
# entrar btn
pyautogui.click(x=713, y=651)

#pyautogui.moveTo(x=1217, y=0)

#pyautogui.click('text.txt')
pyautogui.alert('logado') 

# get position

#position = pyautogui.position()
#print('entrar click',position)


