from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Your Telegram bot token
TOKEN = "8210186257:AAFjuYyNEM78WlEO4knsqmT3j7Sgz7Pu5cs"

# Storage for cashouts (in memory for now)
cashouts = []

# Start command
def start(update, context):
    update.message.reply_text("💸 Cashout Tracker Bot is live!\nType /help to see commands.")

# Help command
def help_command(update, context):
    update.message.reply_text(
        "Here are the commands you can use:\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/cashout <amount> - Record a cashout\n"
        "/total - Show total cashouts"
    )

# Cashout command
def cashout(update, context):
    try:
        amount = float(context.args[0])
        cashouts.append(amount)
        update.message.reply_text(f"✅ Cashout of £{amount} recorded!")
    except (IndexError, ValueError):
        update.message.reply_text("⚠️ Please enter a valid amount. Example: /cashout 50")

# Total command
def total(update, context):
    if cashouts:
        total_amount = sum(cashouts)
        update.message.reply_text(f"💰 Total cashouts: £{total_amount}")
    else:
        update.message.reply_text("No cashouts recorded yet.")

# Echo any text messages
def echo(update, context):
    update.message.reply_text(update.message.text)

# Main bot setup
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

# Handlers
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(CommandHandler("cashout", cashout))
dp.add_handler(CommandHandler("total", total))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

print("Bot started... go to @Jftank_bot")
updater.start_polling()
updater.idle()
