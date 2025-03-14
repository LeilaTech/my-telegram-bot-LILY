from aiogram import Router, types  # Основные классы aiogram для работы с маршрутизатором и сообщениями
from aiogram.filters import Command  # Фильтр для обработки команд
from utils.randomfox import fox  # Утилита для получения изображения случайной лисы
from utils.randomcat import cat  # Утилита для получения изображения случайной кошки
from utils.randomdog import dog  # Утилита для получения изображения случайной собаки
from keyboards.keyboards import kb1, kb2, kb3  # Импорт готовых клавиатур
from random import randint  # Для генерации случайных чисел

# Создаём маршрутизатор для объединения обработчиков сообщений
router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обрабатывает команду /start.
    Отправляет пользователю приветственное сообщение и клавиатуру главного меню.
    """
    await message.answer("Добро пожаловать! Выберите нужный раздел из меню ниже.", reply_markup=kb1)

@router.message(Command("stop"))
async def cmd_stop(message: types.Message):
    """
    Обрабатывает команду /stop.
    Прощается с пользователем.
    """
    await message.answer("До встречи! Спасибо, что использовали меня!")

@router.message(lambda message: message.text.lower() in ["привет", "hello"])
async def cmd_hello(message: types.Message):
    """
    Отвечает на приветственные сообщения ("привет", "hello").
    """
    await message.answer(f"Привет, {message.chat.first_name}! Что вы хотите сделать?", reply_markup=kb1)

@router.message(lambda message: message.text.lower() == "пока")
async def cmd_bye(message: types.Message):
    """
    Отвечает на прощальные сообщения ("пока").
    """
    await message.answer(f"До свидания, {message.chat.first_name}! Возвращайтесь, когда потребуется помощь!", reply_markup=kb1)

@router.message(lambda message: message.text.lower() in ["ты кто", "кто ты"])
async def cmd_who(message: types.Message):
    """
    Отвечает на вопрос "ты кто?" или "кто ты?".
    """
    await message.answer("Я бот, созданный для развлечений и помощи! Чем могу помочь?")

@router.message(lambda message: message.text.lower() in ["животные", "animals"])
async def cmd_animals(message: types.Message):
    """
    Переход в меню выбора животных.
    Показывает кнопки с выбором животных.
    """
    await message.answer("Выберите животное, которое хотите увидеть:", reply_markup=kb2)

@router.message(lambda message: message.text.lower() in ["лиса", "fox"])
async def cmd_fox(message: types.Message):
    """
    Отправляет случайное изображение лисы.
    """
    await message.answer_photo(photo=fox(), caption="Вот ваша лиса!")

@router.message(lambda message: message.text.lower() in ["кошка", "cat", "кот"])
async def cmd_cat(message: types.Message):
    """
    Отправляет случайное изображение кошки.
    """
    await message.answer_photo(photo=cat(), caption="Вот ваша кошка!")

@router.message(lambda message: message.text.lower() in ["собака", "dog"])
async def cmd_dog(message: types.Message):
    """
    Отправляет случайное изображение собаки.
    """
    await message.answer_photo(photo=dog(), caption="Вот ваша собака!")

@router.message(lambda message: message.text.lower() == "игра")
async def cmd_game(message: types.Message):
    """
    Переход в игровое меню.
    Показывает клавиатуру с игровыми функциями.
    """
    await message.answer("Выберите игру из списка ниже:", reply_markup=kb3)

@router.message(lambda message: message.text.lower() == "число")
async def cmd_num(message: types.Message):
    """
    Генерация случайного числа от 1 до 10.
    """
    number = randint(1, 10)
    await message.answer(f"Ваше случайное число: {number}")

@router.message(lambda message: message.text.lower() == "кубик")
async def cmd_kubik(message: types.Message):
    """
    Симулирует бросок кубика и показывает результат.
    """
    await message.answer_dice(emoji="🎲")

@router.message(lambda message: message.text.lower() == "назад")
async def cmd_back(message: types.Message):
    """
    Возвращает пользователя в главное меню.
    """
    await message.answer("Главное меню:", reply_markup=kb1)

@router.message()
async def echo(message: types.Message):
    """
    Обработка других сообщений, не связанных с командами.
    Если сообщение не распознано, текст отправляется обратно.
    """
    user_text = message.text
    if user_text.lower() not in [
        "привет", "hello", "пока", "ты кто", "кто ты", "животные", "animals",
        "лиса", "fox", "кошка", "cat", "кот", "собака", "dog", "игра", "число",
        "кубик", "назад", "главное меню"
    ]:
        # Если команда не распознана, текст преобразуется в голос
        from echo.echo_tts import tts_handler
        await tts_handler(message)
    else:
        # Отправляет текст обратно пользователю
        await message.answer(message.text)
