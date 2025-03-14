import logging  # Логирование ошибок
import os  # Работа с файлами
from aiogram import Router, types  # Основные классы aiogram
from aiogram.types import FSInputFile  # Для отправки файлов
from gtts import gTTS  # Google TTS
from pydub import AudioSegment  # Работа с аудио
from pydub.utils import which  # Настройка ffmpeg

# Устанавливаем путь к ffmpeg
AudioSegment.converter = which("ffmpeg")

# Создаем маршрутизатор
router = Router()

@router.message()
async def tts_handler(message: types.Message):
    """
    Преобразует текст в голосовое сообщение.
    """
    if not message.text:
        return

    try:
        tts = gTTS(text=message.text, lang="ru")
        tts.save("output.mp3")
        audio = AudioSegment.from_mp3("output.mp3")
        audio.export("output.ogg", format="ogg")
        voice = FSInputFile("output.ogg")
        await message.answer_voice(voice=voice)
        os.remove("output.mp3")
        os.remove("output.ogg")
    except Exception as e:
        logging.error(f"Ошибка преобразования текста в речь: {e}")
        await message.answer("Ошибка обработки текста.")
