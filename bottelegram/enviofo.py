
import telebot
import pyautogui
bot = telebot.TeleBot("5774247332:AAFeELsXoIj-KwOf0XmkS3aoTvxVKplDzPQ")

@bot.message_handler(commands=["start","ayuda","help"])

def cmd_start(message):
    bot.reply_to(message, "hola mundo")

@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "comando no disponible")
    else:
        # Capturar pantalla.
        screenshot = pyautogui.screenshot()
        # Guardar imagen.
        screenshot.save("screenshot.png")

        foto = open("C:/Users/111/Documents/holamundo/screenshot.png", "rb")
        bot.send_document(message.chat.id, foto, "lo hiciste perro")


if __name__ == "__main__":
    print("inciando bot")
    bot.infinity_polling()
    print("fin")