from typing import Final
import dotenv
import asyncio
from telegram import Bot

# This file is only to test whether my phone receives notifications from the bot. I'm writing out texts in the cli and checking if I get them on my phone.

TOKEN: Final = dotenv.get_key(dotenv.find_dotenv(), "TOKEN")
CHAT_ID: Final = dotenv.get_key(dotenv.find_dotenv(), "CHAT_ID")

async def main() -> None:
    bot = Bot(token=TOKEN)
    print("Type a message to send. Type 'quit' to stop.")

    while True:
        message = await asyncio.get_event_loop().run_in_executor(None, input, "You: ")

        if message.lower() == "quit":
            break

        if message.strip():
            await bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    asyncio.run(main())
