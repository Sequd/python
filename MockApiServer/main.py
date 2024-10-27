# main.py
from flask import Flask, request, jsonify, make_response, render_template
import json
import os

app = Flask(__name__)

CONFIG_PATH = "config.json"

# Функции для загрузки и сохранения конфигурации
def load_config():
    with open(CONFIG_PATH, encoding="utf-8") as config_file:
        return json.load(config_file)

def save_config(data):
    with open(CONFIG_PATH, "w", encoding="utf-8") as config_file:
        json.dump(data, config_file, ensure_ascii=False, indent=4)

config_data = load_config()

# Функция для подстановки параметров в ответ
def format_response(response_template, params):
    try:
        for key, value in params.items():
            response_template = json.loads(json.dumps(response_template).replace(f"${{{key}}}", value))
        return response_template
    except KeyError:
        return {"error": "Необходимые параметры отсутствуют"}

# Обработчик для отображения UI страницы
@app.route('/', methods=['GET'])
def config_ui():
    return render_template("config.html", endpoints=config_data.get("endpoints", []))

# API для получения всех маршрутов
@app.route('/api/endpoints', methods=['GET'])
def get_endpoints():
    return jsonify(config_data.get("endpoints", []))

# API для добавления или обновления маршрута
@app.route('/api/endpoints', methods=['POST'])
def update_endpoint():
    endpoint_data = request.json
    path = endpoint_data.get("path")
    if not path:
        return jsonify({"error": "Не указан путь маршрута"}), 400

    # Проверка на существование маршрута и обновление данных
    for endpoint in config_data["endpoints"]:
        if endpoint["path"] == path:
            endpoint.update(endpoint_data)
            break
    else:
        config_data["endpoints"].append(endpoint_data)

    save_config(config_data)
    return jsonify({"success": True, "path": path})

# API для удаления маршрута
@app.route('/api/endpoints/<path:path>', methods=['DELETE'])
def delete_endpoint(path):
    config_data["endpoints"] = [ep for ep in config_data["endpoints"] if ep["path"] != f"/{path}"]
    save_config(config_data)
    return jsonify({"success": True, "deleted_path": path})

# Обработчик для обработки GET и POST-запросов
@app.route('/<path:endpoint>', methods=['GET', 'POST'])
def handle_request(endpoint):
    endpoint_config = next((ep for ep in config_data.get("endpoints", []) if ep["path"] == f"/{endpoint}"), None)
    if not endpoint_config or request.method not in endpoint_config["methods"]:
        return jsonify({"error": f"Маршрут не поддерживает {request.method}-запросы"}), 404

    # Проверка обязательных параметров
    params = request.args.to_dict() if request.method == 'GET' else request.json or {}
    missing_params = [p for p in endpoint_config.get("required_params", []) if p not in params]
    if missing_params:
        return jsonify({"error": f"Отсутствуют обязательные параметры: {', '.join(missing_params)}"}), 400

    # Форматирование ответа
    response = format_response(endpoint_config["response"], params)
    return make_response(jsonify(response))

if __name__ == "__main__":
    app.run(host=config_data["host"], port=config_data["port"])
