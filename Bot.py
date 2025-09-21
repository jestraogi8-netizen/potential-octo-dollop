from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Token will be read from environment variable on Render
TOKEN = os.getenv("TOKEN")

def start(update, context):
    update.message.reply_text("Bot is live ✅")

def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

print("Bot started... go to @Jftank_bot and type /start")
updater.start_polling()
updater.idle()"

def start(update, context):
    update.message.reply_text("Bot is live ✅")

def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

print("Bot started... go to @Jftank_bot and type /start")
updater.start_polling()
updater.idle()
