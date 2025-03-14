import logging  # Для логирования работы бота
import asyncio  # Для асинхронного выполнения задач
from aiogram import Bot, Dispatcher  # Основные классы для работы с Telegram API
import config  # Конфигурационный файл для загрузки токена
from handlers import common  # Подключение общих обработчиков
from echo.echo_tts import router as tts_router  # Роутер для текстовых сообщений
import requests  # Для проверки API Telegram

API_TOKEN = config.token  # Загрузка токена из переменной окружения

# Настройка базового логирования
logging.basicConfig(level=logging.INFO)

# Проверка доступности API Telegram
def check_telegram_api(token):
    response = requests.get(f'https://api.telegram.org/bot{token}/getMe')
    if response.status_code == 200:
        print("Telegram API доступен. Информация о боте:")
        print(response.json())
    else:
        print("Ошибка при подключении к Telegram API:")
        print(response.json())
        exit(1)  # Завершить выполнение, если ошибка

check_telegram_api(API_TOKEN)  # Выполняем проверку перед запуском

# Создание экземпляра бота
bot = Bot(token=API_TOKEN)
# Создание экземпляра диспетчера
dp = Dispatcher()

# Подключение обработчиков (роутеров)
dp.include_router(common.router)  # Роутеры для обработки команд
dp.include_router(tts_router)  # Роутеры для обработки текстовых сообщений

async def main():
    """
    Основная функция для запуска бота.
    """
    try:
        # Запуск polling для постоянного получения обновлений от Telegram
        await dp.start_polling(bot)
    finally:
        # Закрытие сессии при завершении работы
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())  # Асинхронный запуск программы
