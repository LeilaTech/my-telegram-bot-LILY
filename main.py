
import logging  # Для логирования работы бота
import asyncio  # Для выполнения асинхронных задач
from aiogram import Bot, Dispatcher  # Основные классы для работы с Telegram API
import config  # Подключение файла config.py для загрузки токена
from handlers import common  # Общие обработчики команд бота
from echo.echo_tts import router as tts_router  # Обработчик текстовых сообщений
import requests  # Для проверки доступности Telegram API
from webhook import app  # Flask-сервер для обработки веб-запросов
from threading import Thread  # Для запуска Flask и Telegram-бота параллельно

# Загрузка токена Telegram-бота из config.py
API_TOKEN = config.token

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Проверка доступности Telegram API
def check_telegram_api(token):
    """
    Проверяет подключение к Telegram API и выводит информацию о боте.
    """
    response = requests.get(f'https://api.telegram.org/bot{token}/getMe')
    if response.status_code == 200:  # Если соединение успешно
        logging.info("Telegram API доступен. Информация о боте:")
        logging.info(response.json())
    else:  # Если есть ошибка, вывести её и завершить выполнение
        logging.error("Ошибка при подключении к Telegram API:")
        logging.error(response.json())
        exit(1)

# Выполняем проверку Telegram API перед запуском
check_telegram_api(API_TOKEN)

# Создаём экземпляры бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Подключение обработчиков (роутеров)
async def register_routers():
    """
    Регистрирует все обработчики (роутеры) для Telegram-бота.
    """
    dp.include_router(common.router)  # Регистрируем общие обработчики
    dp.include_router(tts_router)    # Регистрируем обработчики текстовых сообщений
    logging.info("Обработчики успешно подключены.")

# Асинхронная функция запуска Telegram-бота
async def start_telegram_bot():
    """
    Запускает Telegram-бота с использованием aiogram Dispatcher.
    """
    await register_routers()  # Регистрируем обработчики
    logging.info("Запуск Telegram-бота...")
    await dp.start_polling(bot)  # Начинаем опрос Telegram API для получения новых сообщений

# Функция запуска Flask-сервера
def start_flask():
    """
    Запускает Flask-сервер в отдельном потоке.
    """
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    # Запускаем Flask-сервер в отдельном потоке
    flask_thread = Thread(target=start_flask)
    flask_thread.start()

    # Логируем успешный запуск Flask
    logging.info("Flask-сервер запущен. Запускаем Telegram-бота...")

    # Запускаем Telegram-бота в основном потоке
    asyncio.run(start_telegram_bot())
