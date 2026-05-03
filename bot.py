import telebot
import pandas as pd
import requests

# إعدادات البوت - ضع التوكن الخاص بك هنا
API_TOKEN = '8750825634:AAEsypkMsUFAjywAq8ayhsjz96KSHzP6JcE'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🚀 **MTG INVESTMENT RADAR IS LIVE**\n"
        "──────────────────\n"
        "أهلاً بك يا دكتور في نظامك الخاص. الرادار يعمل الآن ويراقب الأسواق.\n"
        "سيتم إرسال الصفقات فور تحقق شروط الـ 5 نجوم."
    )
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

# تشغيل البوت
if __name__ == "__main__":
    print("MTG Radar is running...")
    bot.infinity_polling()
  
