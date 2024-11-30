from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# التوكن الخاص بالبوت
bot_token = '7546741251:AAFe0ynVnQfODznUSRAAuRBEmJUvu35EP9c'

# دالة البدء التي ترسل رسالة ترحيب
def start(update, context):
    update.message.reply_text("Hello! I'm your bot.")

# دالة الرد على الرسائل
def echo(update, context):
    text = update.message.text
    update.message.reply_text(f'You said: {text}')

# إعداد البوت واستخدام Polling
def main():
    # إعداد Updater وBot
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # إضافة معالجي الأوامر
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # إضافة معالج للرسائل
    echo_handler = MessageHandler(Filters.text & ~Filters.command, echo)
    dispatcher.add_handler(echo_handler)

    # بدء الـ polling
    updater.start_polling()

    # تشغيل البوت حتى يتم إيقافه يدويًا
    updater.idle()

if __name__ == '__main__':
    main(), host='0.0.0.0', port=8000)
