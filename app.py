import json
from flask import Flask, request
import requests

app = Flask(__name__)

# === 텔레그램 설정 ===
TELEGRAM_TOKEN = '7423718072:AAHxxxeRI0PP9WiMvIgqly-RWfUMZW8-PRQ'
TELEGRAM_CHAT_ID = '7766036627'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Telegram Error: {e}")

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', '📡 알 수 없는 알림')
    send_telegram_message(message)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)



















