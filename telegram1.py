import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# إعداد التوكن الخاص بك
TOKEN = "7546741251:AAFe0ynVnQfODznUSRAAuRBEmJUvu35EP9c"

# تعريف أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً! أنا بوت تيليجرام الخاص بك.")

def main():
    # إنشاء التطبيق
    application = Application.builder().token(TOKEN).build()

    # إضافة أوامر
    application.add_handler(CommandHandler("start", start))

    # تشغيل البوت
    application.run_polling()

if __name__ == "__main__":
    main()
