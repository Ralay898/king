from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from telegram import Bot
from telegram.ext import Updater, CommandHandler

# إعداد البوت
TOKEN = "7546741251:AAFe0ynVnQfODznUSRAAuRBEmJUvu35EP9c"

def start(update, context):
    update.message.reply_text("مرحبا بك في بوت عمران!")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))

# تشغيل خادم ويب وهمي
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_server():
    server = HTTPServer(('0.0.0.0', 8000), HealthCheckHandler)
    server.serve_forever()

if __name__ == "__main__":
    # تشغيل خادم الصحة في خيط مستقل
    Thread(target=run_server, daemon=True).start()
    print("Health check server is running on port 8000...")
    
    # تشغيل البوت
    print("Bot is running...")
    updater.start_polling()
    updater.idle()
