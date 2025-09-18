import telebot as tl

bot = tl.TeleBot('8467658943:AAHfyHgsfXBH0xY77HQxNiG_uOldskIOHbQ')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Hi")

bot.polling(non_stop=True)
