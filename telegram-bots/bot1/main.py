import telegram
import asyncio

bot = telegram.Bot(token='7536148506:AAGk7nFwWDVHKs0t4kimZ3twPAMqbCuHD9c')
chat_id = '-1002443507373'  # Мед. Личные доки
# chat_id = '343178783'  # Bot


async def post_to_channel(message):
    try:
        await bot.send_message(chat_id=chat_id, text=message)
        print(f"Сообщение '{message}' отправлено в канал.")
    except telegram.error.TelegramError as e:
        print(f"Ошибка отправки сообщения: {e}")


async def main():
    while True:
        message_to_post = "Текст сообщения для публикации."  # Ваше сообщение
        await post_to_channel(message_to_post)  # Ожидание отправки сообщения
        await asyncio.sleep(3600)  # Асинхронная пауза в 1 час


if __name__ == "__main__":
    asyncio.run(main())
