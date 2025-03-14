import os  # Для работы с переменными окружения
import sys  # Для завершения программы при ошибках

# Получение токена из переменных окружения
try:
    token = os.environ['BOT_TOKEN']  # Чтение токена
    if not token:  # Проверка, что токен не пустой
        raise ValueError("Токен не может быть пустым")
except KeyError:
    # Вывод ошибки, если переменной нет
    print("Ошибка: BOT_TOKEN не найден в переменных окружения")
    print("Добавьте BOT_TOKEN в Secrets (Tools -> Secrets)")
    sys.exit(1)  # Завершаем программу
except ValueError as e:
    # Вывод ошибки, если токен пуст
    print(f"Ошибка: {e}")
    sys.exit(1)
