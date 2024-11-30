from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# التوكن الخاص بالبوت
bot_token = '7546741251:AAFe0ynVnQfODznUSRAAuRBEmJUvu35EP9c'

# دالة البدء التي ترسل رسالة ترحيب
async def start(update: Update, context):
    await update.message.reply_text("Hello! I'm your bot.")

# دالة الرد على الرسائل
async def echo(update: Update, context):
    text = update.message.text
    await update.message.reply_text(f'You said: {text}')

# إعداد البوت واستخدام Polling
def main():
    # إعداد Application و Bot
    application = Application.builder().token(bot_token).build()

    # إضافة معالجي الأوامر
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # إضافة معالج للرسائل
    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(echo_handler)

    # بدء الـ polling
    application.run_polling()

if __name__ == '__main__':
    main()
