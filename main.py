import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

def start(update, context): 
    update.message.reply_text( 
        "Hello, Welcome to Kurmato") 

def helps(update, context):
  update.message.reply_text(
      """
      Hi there! I'm Telegram bot created by Pranav. Please follow these commands:-

      /start -> Welcome to the Kurmato!
      /help -> This particular message
      /content -> To know more about kurmato, visit the website
      /contact -> contact information

      I hope this helps
      """)

def content(update, context):
  update.message.reply_text('Kurmato website: https://kurmato.com/')

def contact(update, context):
  update.message.reply_text('Our contact information is on the website')

updater = telegram.ext.Updater(TOKEN, 
                  use_context=True) 

dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start', start))
dispatch.add_handler(telegram.ext.CommandHandler('help', helps))
dispatch.add_handler(telegram.ext.CommandHandler('content', content))
dispatch.add_handler(telegram.ext.CommandHandler('contact', contact))

dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.ext,handle_message))

updater.start_polling()
updater.idle()