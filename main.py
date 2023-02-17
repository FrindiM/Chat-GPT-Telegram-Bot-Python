import telegram
from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import openai
TELEGRAM_TOKEN = 'Telegram Token'
OPENAI_API_KEY = 'OpenAI API'

bot = telegram.Bot(token=TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

# Fungsi untuk menangani pesan yang diterima
def handle_message(update: Update, context: CallbackContext):
    # Mengambil ID chat pengguna dari objek Update
    chat_id = update.effective_chat.id

    # Membuat objek bot dari konteks
    bot: Bot = context.bot

    # Mengambil teks pesan yang diterima
    text = update.message.text

    response = openai.Completion.create(
        engine='davinci',
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Membalas pesan yang diterima dengan pesan yang sama
    bot.send_message(chat_id=chat_id, text=response.choices[0].text)

# Membuat objek Updater dan menambahkan handler
updater = Updater(token = TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Menambahkan handler untuk menangani pesan yang diterima
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

# Memulai polling update
updater.start_polling()
