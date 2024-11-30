from flask import Flask, request
import telegram

app = Flask(__name__)

# إضافة التوكن الخاص بالبوت
bot = telegram.Bot(token='7546741251:AAFe0ynVnQfODznUSRAAuRBEmJUvu35EP9c')

@app.route('/webhook', methods=['POST'])
def webhook():
    # استلام البيانات من تيليجرام
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    
    # استخراج الرسالة من الـ update
    chat_id = update.message.chat_id
    text = update.message.text
    
    # إرسال الرد على الرسالة
    bot.sendMessage(chat_id=chat_id, text=f'You said: {text}')
    
    # إعادة OK كإجابة على الويب هوك
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
