import pyautogui
import os
from os import remove
import time

# Capturar pantalla.
#screenshot = pyautogui.screenshot()
# Guardar imagen.
#screenshot.save("C:/Users/111/Downloads/screenshot.png")
#time.sleep(1)
screenshot = pyautogui.screenshot()
user_profile = os.environ["USERPROFILE"]
user_dowload = user_profile + "\Downloads" + "\screenshot.png"
print (user_dowload)
print (user_profile)
print (user_profile[9:100])

screenshot.save(user_dowload)


foto = open(user_dowload, "rb")
foto.close()
time.sleep(1)
remove(user_dowload)

#os.system("calc.exe")

#tm = "C:\Program Files\TeamViewer\TeamViewer.exe"
#os.startfile(tm)
