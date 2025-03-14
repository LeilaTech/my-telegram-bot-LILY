from flask import Flask, request
import os
import subprocess  # Для выполнения команды обновления репозитория
import hmac
import hashlib

app = Flask(__name__)

# Получение секретного ключа из переменной окружения
SECRET = os.environ.get('WEBHOOK_SECRET', 'default_secret_key')  # Добавьте ключ в Render

@app.route('/')
def home():
    """
    Проверка статуса сервера.
    """
    return "Сервер работает!"

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    """
    Обработка запросов от GitHub Webhook. Выполняет обновление репозитория через `git pull`.
    """
    try:
        signature = request.headers.get('X-Hub-Signature-256')
        if not signature:
            return "Подпись отсутствует", 400

        computed_hmac = 'sha256=' + hmac.new(SECRET.encode(), request.data, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(computed_hmac, signature):
            return "Неверная подпись", 403

        payload = request.json
        if not payload:
            return "Пустой запрос", 400

        result = subprocess.run(['git', 'pull', 'origin', 'main'], capture_output=True, text=True)
        if result.returncode == 0:
            return f"Git pull выполнен: {result.stdout}", 200
        else:
            return f"Ошибка выполнения git pull: {result.stderr}", 500

    except Exception as e:
        return f"Ошибка обработки вебхука: {e}", 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)