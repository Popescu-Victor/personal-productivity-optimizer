from typing import Final
import dotenv
from telegram import Bot
from telegram import Update


TOKEN: Final = dotenv.get_key(dotenv.find_dotenv(), "TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I am accute bot!")



async def first_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This is the first message!")



def handle_response(text: str) -> str:
    text = text.lower()

    if "hello" in text:
        return "Hello there!"

