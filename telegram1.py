from flask import Flask
from telegram.ext import Application, CommandHandler
import asyncio

# إعداد البوت
TOKEN = "7546741251:AAFe0ynVnQfODznUSRAAuRBEmJUvu35EP9c"
app = Application.builder().token(TOKEN).build()

# تعريف أمر بسيط
async def start(update, context):
    await update.message.reply_text("Hello! I'm running on Flask and Telegram.")

app.add_handler(CommandHandler("start", start))

# إعداد Flask
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running!"

# تشغيل Flask والبوت
if __name__ == "__main__":
    # تشغيل Telegram bot في نفس الخيط
    async def run_telegram():
        await app.run_polling()

    loop = asyncio.get_event_loop()
    loop.create_task(run_telegram())

    # تشغيل Flask
    flask_app.run(host="0.0.0.0", port=8000)
