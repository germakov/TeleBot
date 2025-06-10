import logging

import telebot

from config import TG_BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(TG_BOT_TOKEN)


try:

    @bot.message_handler(content_types=["text", "document", "audio"])
    def get_text_messages(message):
        if message.text == "Привет":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши привет")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")

    logger.info("Бот запущен успешно...")
    bot.polling(non_stop=True, interval=0)
except Exception as e:
    logger.error(f"Ошибка при запуске - {e}")
