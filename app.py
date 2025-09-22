import os
from flask import Flask, request
import requests

app = Flask(__name__)

# Настройки Telegram
BOT_TOKEN = "8467658943:AAHfyHgsfXBH0xY77HQxNiG_uOldskIOHbQ"
CHAT_ID = "5744958521"

def send_to_telegram(ip):
    text = f"Новый переход! IP: {ip}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

@app.route("/")
def index():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    send_to_telegram(ip)
    return f"<h2>Ваш IP: {ip}</h2>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render передаёт порт через переменную
    app.run(host="0.0.0.0", port=port)