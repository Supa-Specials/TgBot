import telebot as tl
from deep_translator import GoogleTranslator

bot = tl.TeleBot('8467658943:AAHfyHgsfXBH0xY77HQxNiG_uOldskIOHbQ')

@bot.message_handler(commands=['start'])
def Greeting(message):
    bot.send_message(message.chat.id, "Hi")

@bot.message_handler(commands=['translate'])
def translate_text(message):
    text = message.text.replace('/translate', '').strip()
    if not text:
        bot.send_message(message.chat.id, "Пожалуйста, добавь текст после команды /translate.")
        return

    try:
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        bot.send_message(message.chat.id, f"Перевод: {translated}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка перевода: {e}")

bot.polling(non_stop=True)