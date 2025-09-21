from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "8210186257:AAFjuYyNEM78WlEO4knsqmT3j7Sgz7Pu5cs"

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
