from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# إعداد التوكن الخاص بالبوت
TOKEN = "7546741251:AAFe0ynVnQfODznUSRAAuRBEmJUvu35EP9c"

# إنشاء تطبيق Flask
app = Flask(__name__)

# صفحة رئيسية وهمية لمتطلبات Koyeb
@app.route("/")
def home():
    return "The Telegram Bot is running on Koyeb!"

# دالة الرد على أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام عليكم، انا بوت عمران!")

# تشغيل البوت
async def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import threading
    import asyncio

    # تشغيل بوت تيليجرام في خيط منفصل
    bot_thread = threading.Thread(target=lambda: asyncio.run(run_bot()), daemon=True)
    bot_thread.start()

    # تشغيل تطبيق Flask
    app.run(host="0.0.0.0", port=8000)
