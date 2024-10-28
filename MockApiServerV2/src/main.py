from flask import Flask, request, jsonify, render_template
import json
import logging
from typing import Dict, Any
import os
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import MethodNotAllowed, NotFound

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DynamicRouter:
    def __init__(self):
        self.endpoints = {}

    def add_endpoint(self, path: str, config: dict):
        self.endpoints[path] = config

    def remove_endpoint(self, path: str):
        if path in self.endpoints:
            del self.endpoints[path]

    def get_endpoint(self, path: str) -> Dict:
        return self.endpoints.get(path)

    def handle_request(self, path: str):
        endpoint_config = self.get_endpoint(path)
        if not endpoint_config:
            raise NotFound()

        if request.method not in endpoint_config['methods']:
            raise MethodNotAllowed()

        try:
            params = request.args if request.method == 'GET' else request.get_json() or {}

            required_params = endpoint_config.get('required_params', [])
            if not all(param in params for param in required_params):
                return jsonify({'error': f'Missing required parameters: {required_params}'}), 400

            response = json.loads(json.dumps(endpoint_config['response']))
            for key, value in response.items():
                if isinstance(value, str) and value.startswith('$'):
                    param_name = value[1:]
                    response[key] = params.get(param_name, value)
            return jsonify(response)
        except Exception as e:
            logger.error(f"Error handling request: {str(e)}")
            return jsonify({'error': 'Internal server error'}), 500


class MockAPIServer:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self._load_config(config_path)
        self.app = Flask(__name__)
        self.router = DynamicRouter()
        self._setup_routes()
        self._setup_admin_routes()

        # Регистрируем обработчик для всех запросов
        self.app.before_request(self._handle_dynamic_routes)

    def _handle_dynamic_routes(self):
        if request.path.startswith('/api/endpoints') or request.path == '/':
            return None

        try:
            return self.router.handle_request(request.path)
        except NotFound:
            return None  # Позволяем Flask продолжить поиск других маршрутов
        except MethodNotAllowed:
            return jsonify({'error': 'Method not allowed'}), 405

    def _load_config(self, config_path: str) -> dict:
        """Загрузка конфигурации из JSON файла."""
        try:
            if not os.path.exists(config_path):
                return {"host": "localhost", "port": 8000, "endpoints": []}
            with open(config_path) as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Ошибка загрузки конфигурации: {e}")
            raise

    def _save_config(self):
        """Сохранение текущей конфигурации в файл."""
        try:
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
            with open(self.config_path, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            logger.error(f"Ошибка сохранения конфигурации: {e}")
            raise

    def _validate_endpoint_config(self, endpoint_config: Dict) -> tuple[bool, str]:
        """Валидация конфигурации эндпоинта."""
        required_fields = ['path', 'methods', 'response']
        if not all(field in endpoint_config for field in required_fields):
            return False, f"Missing required fields: {', '.join(required_fields)}"

        if not endpoint_config['path'].startswith('/'):
            return False, "Path must start with /"

        valid_methods = {'GET', 'POST', 'PUT', 'DELETE', 'PATCH'}
        invalid_methods = [m for m in endpoint_config['methods'] if m not in valid_methods]
        if invalid_methods:
            return False, f"Invalid HTTP methods: {', '.join(invalid_methods)}"

        try:
            json.dumps(endpoint_config['response'])
        except Exception:
            return False, "Response must be valid JSON"

        return True, ""

    def _setup_admin_routes(self):
        """Настройка маршрутов для административного интерфейса."""

        @self.app.route('/')
        def admin_panel():
            return render_template('config.html')

        @self.app.route('/api/endpoints', methods=['GET'])
        def get_endpoints():
            return jsonify(self.config.get('endpoints', []))

        @self.app.route('/api/endpoints', methods=['POST'])
        def add_endpoint():
            try:
                endpoint_config = request.get_json()

                is_valid, error_message = self._validate_endpoint_config(endpoint_config)
                if not is_valid:
                    return jsonify({'error': error_message}), 400

                existing_endpoints = [e for e in self.config['endpoints']
                                      if e['path'] == endpoint_config['path']]
                if existing_endpoints:
                    return jsonify({'error': 'Endpoint with this path already exists'}), 400

                if 'endpoints' not in self.config:
                    self.config['endpoints'] = []
                self.config['endpoints'].append(endpoint_config)
                self._save_config()

                # Добавляем эндпоинт в динамический роутер
                self.router.add_endpoint(endpoint_config['path'], endpoint_config)

                return jsonify({'message': 'Endpoint added successfully'})
            except Exception as e:
                logger.error(f"Error adding endpoint: {str(e)}")
                return jsonify({'error': str(e)}), 500

        @self.app.route('/api/endpoints/<path:endpoint_path>', methods=['PUT'])
        def update_endpoint(endpoint_path):
            try:
                endpoint_config = request.get_json()

                is_valid, error_message = self._validate_endpoint_config(endpoint_config)
                if not is_valid:
                    return jsonify({'error': error_message}), 400

                endpoint_found = False
                for i, endpoint in enumerate(self.config['endpoints']):
                    if endpoint['path'] == f"/{endpoint_path}":
                        self.config['endpoints'][i] = endpoint_config
                        endpoint_found = True
                        break

                if not endpoint_found:
                    return jsonify({'error': 'Endpoint not found'}), 404

                self._save_config()

                # Обновляем эндпоинт в динамическом роутере
                self.router.remove_endpoint(endpoint_config['path'])
                self.router.add_endpoint(endpoint_config['path'], endpoint_config)

                return jsonify({'message': 'Endpoint updated successfully'})
            except Exception as e:
                logger.error(f"Error updating endpoint: {str(e)}")
                return jsonify({'error': str(e)}), 500

        @self.app.route('/api/endpoints', methods=['DELETE'])
        def delete_endpoint():
            try:
                path = request.args.get('path')
                if not path:
                    return jsonify({'error': 'Path parameter is required'}), 400

                original_length = len(self.config['endpoints'])
                self.config['endpoints'] = [e for e in self.config['endpoints']
                                            if e['path'] != path]

                if len(self.config['endpoints']) == original_length:
                    return jsonify({'error': 'Endpoint not found'}), 404

                self._save_config()

                # Удаляем эндпоинт из динамического роутера
                self.router.remove_endpoint(path)

                return jsonify({'message': 'Endpoint deleted successfully'})
            except Exception as e:
                logger.error(f"Error deleting endpoint: {str(e)}")
                return jsonify({'error': str(e)}), 500

    def _setup_routes(self):
        """Настройка начальных маршрутов из конфигурации."""
        for endpoint in self.config.get('endpoints', []):
            self.router.add_endpoint(endpoint['path'], endpoint)

    def run(self):
        """Запуск сервера."""
        logger.info(f"Запуск сервера на {self.config.get('host', 'localhost')}:{self.config.get('port', 8000)}")
        self.app.run(
            host=self.config.get('host', 'localhost'),
            port=self.config.get('port', 8000)
        )


if __name__ == "__main__":
    server = MockAPIServer("config/config.json")
    server.run()