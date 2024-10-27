from flask import Flask, request, jsonify
import json
import logging
from typing import Dict, Any

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MockAPIServer:
    def __init__(self, config_path: str):
        self.config = self._load_config(config_path)
        self.app = Flask(__name__)
        self._setup_routes()

    def _load_config(self, config_path: str) -> dict:
        """Загрузка конфигурации из JSON файла."""
        try:
            with open(config_path) as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Ошибка загрузки конфигурации: {e}")
            raise

    def _setup_routes(self):
        """Настройка маршрутов на основе конфигурации."""
        for endpoint in self.config.get('endpoints', []):
            self._create_endpoint(endpoint)

    def _create_endpoint(self, endpoint_config: Dict[str, Any]):
        """Создание endpoint'а на основе конфигурации."""

        def endpoint_handler():
            # Получение параметров из запроса
            params = request.args if request.method == 'GET' else request.get_json() or {}

            # Проверка метода
            if request.method not in endpoint_config['methods']:
                return jsonify({'error': 'Method not allowed'}), 405

            # Проверка обязательных параметров
            required_params = endpoint_config.get('required_params', [])
            if not all(param in params for param in required_params):
                return jsonify({'error': 'Missing required parameters'}), 400

            # Формирование ответа на основе шаблона
            response = json.loads(json.dumps(endpoint_config['response']))
            for key, value in response.items():
                if isinstance(value, str) and value.startswith('$'):
                    param_name = value[1:]
                    response[key] = params.get(param_name, value)

            return jsonify(response)

        # Регистрация endpoint'а
        self.app.add_url_rule(
            endpoint_config['path'],
            endpoint_config['path'],
            endpoint_handler,
            methods=endpoint_config['methods']
        )

    def run(self):
        """Запуск сервера."""
        logger.info(f"Запуск сервера на {self.config['host']}:{self.config['port']}")
        self.app.run(
            host=self.config['host'],
            port=self.config['port']
        )


if __name__ == "__main__":
    server = MockAPIServer("config/config.json")
    server.run()