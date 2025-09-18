import telebot as tl
import requests
from deep_translator import GoogleTranslator

bot = tl.TeleBot('8467658943:AAHfyHgsfXBH0xY77HQxNiG_uOldskIOHbQ')


def generate_image(prompt):
    url = "https://huggingface.co/spaces/stabilityai/stable-diffusion"
    api_url = "https://hf.space/embed/stabilityai/stable-diffusion/+/api/predict"

    payload = {
        "data": [prompt]
    }

    response = requests.post(api_url, json=payload)
    result = response.json()

    # Получаем ссылку на изображение
    image_url = result['data'][0]  # это URL на CDN Hugging Face

    return image_url

@bot.message_handler(commands=['generate_image'])
def handle_image(message):
    prompt = message.text.replace('/generate_image ', '')
    image_url = generate_image(prompt)
    bot.send_photo(message.chat.id, image_url)


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