from telegram import Bot

API_TOKEN = "7536148506:AAGk7nFwWDVHKs0t4kimZ3twPAMqbCuHD9c"

# Токен бот-API
bot = Bot(token=API_TOKEN)


async def get_chat_id():
    updates = await bot.get_updates()
    for update in updates:
        print(update)


import asyncio

asyncio.run(get_chat_id())
