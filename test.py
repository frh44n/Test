from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Use your actual bot token here
TOKEN = '7457740388:AAF6r_a3KSO3Ewnief127635DBAdKn237AI'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    await update.message.reply_text(f'Hello, {user.first_name}! Welcome to the bot!')

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))

    application.run_polling()

if __name__ == '__main__':
    main()
