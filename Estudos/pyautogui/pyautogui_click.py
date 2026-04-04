import pyautogui
import pyperclip
import time
from datetime import datetime
import sys


pyautogui.alert('logado') 
sys.exit()


hora_atual = datetime.now().strftime("%H:%M:%S")
pyautogui.PAUSE = 1

win = (42, 1047)
notepad = (705, 405)


#time.sleep(2)

pyautogui.moveTo(42, 1047, duration=1)  # Move em 1 segundo
pyautogui.click()



pyautogui.moveTo(notepad, duration=1)  # Move em 1 segundo
pyautogui.click()

time.sleep(0.5)  # Pequena pausa para garantir que o foco esteja correto

pyautogui.write("OI ISABELLA", interval=0.1)  # Digita com intervalo entre as teclas
pyautogui.press("enter")  # Pressiona Enter após digitar

#pyperclip.copy("OI BABY SOOKIE")
#pyautogui.hotkey('ctrl', 'v')



# posição atual do mouse

time.sleep(3)  # Dá tempo para posicionar o mouse
#print(pyautogui.position())
sys.exit() # sai do script




