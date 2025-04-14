from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters

API_TOKEN = '7536148506:AAGk7nFwWDVHKs0t4kimZ3twPAMqbCuHD9c'


async def get_chat_id(update: Update, context) -> None:
    chat_id = update.effective_chat.id
    print(f"Chat ID: {chat_id}")
    await update.message.reply_text(f"Ваш Chat ID: {chat_id}")


if __name__ == "__main__":
    app = ApplicationBuilder().token(API_TOKEN).build()

    # Обработчик сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_chat_id))

    print("Бот запущен. Напишите боту любое сообщение для получения Chat ID.")
    app.run_polling()
