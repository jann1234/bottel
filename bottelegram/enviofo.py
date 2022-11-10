import os
from os import remove
import time
import pyautogui
import telebot
from telebot import types


user_profile = os.environ["USERPROFILE"]
user_dowload = user_profile + "\Downloads" + "\scr.png"
user_telegram = user_profile + "\AppData\Roaming\Telegram Desktop\Telegram.exe"

token_papa = str("5774247332:AAFeELsXoIj-KwOf0XmkS3aoTvxVKplDzPQ")
token_pabed = str("5652820688:AAHbMQWnEx4-oKJYhAukDknpda_hfLfawV0")
token_dasam = str("5686706507:AAEn09IV5QCYcHFDhOIyVHK770burA045ew")
token_otro = str("5709063652:AAET6UzN0BMeFLZMbfdYUrUtjay70cznqxc")

tok = user_profile[9:100]
if tok == "111":
    token = token_papa
elif tok == "pabed":
    token = token_pabed
elif tok == "DASAM":
    token = token_dasam
else :
    token = token_otro    

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start","ayuda","help"])

def cmd_start(message):
    bot.reply_to(message, "FUNCIONANDO")
    m = message.chat.id
    print(m)

@bot.message_handler(commands=["captura"])

def cmd_start(message):
    bot.send_message(message.chat.id, "tomando captura")
    

    # Capturar pantalla.
    screenshot = pyautogui.screenshot()
    # Guardar imagen.
    screenshot.save(user_dowload)


    foto = open(user_dowload, "rb")
    bot.send_document(message.chat.id, foto, caption="captura lista")
    foto.close()
    remove(user_dowload)


@bot.message_handler(commands=["calculadora"])

def cmd_cal(calc):
    os.system("calc.exe")
   

@bot.message_handler(commands=["teamviwer"])

def cmd_cal(team):
    bot.send_message(549266543, "iniciando team wiever")
    tm = "C:/Program Files/TeamViewer/TeamViewer.exe"
    os.startfile(tm)

@bot.message_handler(commands=["telegram"])

def cmd_cal(telg):
    bot.send_message(549266543, "iniciando telegram")
    telg = user_telegram
    os.startfile(telg)

@bot.message_handler(commands=["apagar"])

def cmd_cal(apagar):
    bot.send_message(549266543, "Apagando PC en 15 segundos")
    os.system("shutdown /s /f /t 15")
   

@bot.message_handler(commands=["reiniciar"])

def cmd_cal(apagar):
    bot.send_message(549266543, "Reiniciando PC en 15 segundos")
    os.system("shutdown /r /f /t 15")

@bot.message_handler(commands=["cancelar"])

def cmd_cal(cancelar):
    bot.send_message(549266543, "Cancelando apagado")
    os.system("shutdown /a")

@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "comando no disponible")
    else:
        bot.send_message(message.chat.id, "comando disponible")
        


if __name__ == "__main__":
   
    bot.send_message(549266543, "iniciando pc")

    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('/start')
    itembtn2 = types.KeyboardButton('/captura')
    itembtn3 = types.KeyboardButton('/calculadora')
    itembtn4 = types.KeyboardButton('/teamviwer')
    itembtn5 = types.KeyboardButton('/telegram')
    itembtn6 = types.KeyboardButton('/apagar')
    itembtn7 = types.KeyboardButton('/cancelar')
    itembtn8 = types.KeyboardButton('/reiniciar')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)
    
    bot.send_message(549266543, "Choose one letter:", reply_markup=markup)

    print("inciando bot")
    bot.infinity_polling()
    print("fin")