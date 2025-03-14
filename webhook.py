from flask import Flask, request
import os
import subprocess  # Для более безопасного выполнения команды

app = Flask(__name__)

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    """
    Этот маршрут обрабатывает POST-запросы от GitHub Webhook.
    Выполняется команда для автоматического обновления репозитория.
    """
    try:
        # Проверяем, что запрос пришел от GitHub
        payload = request.json
        if payload:
            # Выполняем обновление репозитория
            result = subprocess.run(['git', 'pull', 'origin', 'main'], capture_output=True, text=True)
            return f"Git pull выполнен: {result.stdout}", 200
        else:
            return "Пустой запрос", 400
    except Exception as e:
        return f"Ошибка обработки вебхука: {e}", 500

if __name__ == '__main__':
    # Используем переменную окружения PORT, если она задана
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
