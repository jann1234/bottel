
import os

import pyautogui
import telebot

bot = telebot.TeleBot("5774247332:AAFeELsXoIj-KwOf0XmkS3aoTvxVKplDzPQ")

@bot.message_handler(commands=["start","ayuda","help"])

def cmd_start(message):
    bot.reply_to(message, "hola mundo")


@bot.message_handler(commands=["captura"])

def cmd_start(message):
    bot.send_message(message.chat.id, "tomando captura")
    m = message.chat.id
    print(m)

     # Capturar pantalla.
    screenshot = pyautogui.screenshot()
        # Guardar imagen.
    screenshot.save("C:/Users/111/Downloads/screenshot.png")


    foto = open("C:/Users/111/Downloads/screenshot.png", "rb")
    bot.send_document(message.chat.id, foto, "captura lista")

@bot.message_handler(commands=["calc"])

def cmd_cal(calc):
    os.system("calc.exe")
   

@bot.message_handler(commands=["team"])

def cmd_cal(team):
    bot.send_message(549266543, "iniciando team wiever")
    tm = "C:/Program Files/TeamViewer/TeamViewer.exe"
    os.startfile(tm)
@bot.message_handler(commands=["apagar"])

def cmd_cal(apagar):
    os.system("shutdown /s /f /t 30")

@bot.message_handler(commands=["cancelar"])

def cmd_cal(cancelar):
    os.system("shutdown /a")

@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "comando no disponible")
    else:
   
        #foto = open("C:/Users/111/Documents/holamundo/screenshot.png", "rb")
        bot.send_document(message.chat.id, foto, "lo hiciste perro")


if __name__ == "__main__":
   
    bot.send_message(549266543, "iniciando pc")

    print("inciando bot")
    bot.infinity_polling()
    print("fin")
