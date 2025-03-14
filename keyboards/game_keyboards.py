from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # Для создания игровой клавиатуры

def make_row_keyboard(buttons: list[str]) -> ReplyKeyboardMarkup:
    """
    Создаёт клавиатуру с кнопками в одну строку.
    """
    row = [KeyboardButton(text=button) for button in buttons]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
