import pyautogui
import pyperclip
import time
from datetime import datetime
import sys


hora_atual = datetime.now().strftime("%H:%M:%S")
pyautogui.PAUSE = 2

time.sleep(2)

# pegar posicai
"""
x = pyautogui.position()
print(x)

sys.exit() # sai do script

"""



pyautogui.hotkey('ctrl', 't')
pyperclip.copy("https://mail.google.com/mail/u/1/")
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey("enter")

# clicar botao escrever
pyautogui.click(x=95, y=258)

# colocar email do destinatário (tab)
pyperclip.copy("geraldo.filho92@hotmail.com")
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey("tab")

# colocar assunto (tab)
pyperclip.copy(f"Hora atual: {hora_atual}")
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey("tab")

# corpo do email



emailbody = f"""
Fazer sua parte
gerado em: {hora_atual}
"""

pyperclip.copy(emailbody)
pyautogui.hotkey('ctrl', 'v')

# clicar no botão enviar
pyautogui.click(x=1216, y=974) # tela notebook


