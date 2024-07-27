from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your bot's token
TOKEN = '7457740388:AAF6r_a3KSO3Ewnief127635DBAdKn237AI'

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f'Hello, {user.first_name}! Welcome to the bot!')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
