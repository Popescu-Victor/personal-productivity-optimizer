from typing import Final
import dotenv
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = dotenv.get_key(dotenv.find_dotenv(), "TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I am accute bot!")

async def first_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This is the first message!")

def handle_response(text: str) -> str:
    text = text.lower()
    if "hello" in text:
        return "Hello there!"
    return "I don't understand that."  # ← you need a default return

# ← you need this to actually process and reply to messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = handle_response(update.message.text)
    await update.message.reply_text(response)

# ← you need a main function to start the bot
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))          # handles /start
    app.add_handler(MessageHandler(filters.TEXT, handle_message))  # handles messages

    print("Bot is running...")
    app.run_polling()