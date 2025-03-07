import telebot
from api.main import app  # Connect to FastAPI backend

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Processing your request...")

bot.polling()
