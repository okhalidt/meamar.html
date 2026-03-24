
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# بيانات بوت تليجرام الخاص بك (المستخرجة من كودك القديم)
TOKEN = "8669811855:AAGvhpikwaC14E_d1fy24J1iyUgAdInXmSg"
CHAT_ID = "7214473798"

def send_telegram_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

@app.route('/')
def home():
    # إرسال إشعار عند دخول أي شخص للموقع
    send_telegram_msg("🔒 تنبيه: شخص ما دخل إلى لوحة تحكم VPN عبد الرحمن!")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
