from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # Для создания клавиатуры

# Главная клавиатура
kb1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Животные"), KeyboardButton(text="Игра")],
        [KeyboardButton(text="/stop")]
    ],
    resize_keyboard=True
)

# Клавиатура выбора животных
kb2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Лиса"), KeyboardButton(text="Кошка"), KeyboardButton(text="Собака")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Игровая клавиатура
kb3 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Число"), KeyboardButton(text="Кубик")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)
