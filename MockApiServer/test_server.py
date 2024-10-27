# test_mock_server.py
import requests

# Базовый URL для локального сервера
BASE_URL = "http://localhost:5000"


# Тест для GET-запроса
def test_get_request():
    url = f"{BASE_URL}/example"
    params = {"param1": "value1", "param2": "value2"}

    response = requests.get(url, params=params)

    assert response.status_code == 200, "Статус код должен быть 200"
    response_data = response.json()

    # Проверяем, что ответ содержит сообщение и переданные параметры
    assert response_data.get("message") == "Это ответ на GET-запрос для /example"
    assert response_data.get("received_params") == params


# Тест для POST-запроса
def test_post_request():
    url = f"{BASE_URL}/example"
    data = {"param1": "value1", "param2": "value2"}

    response = requests.post(url, json=data)

    assert response.status_code == 200, "Статус код должен быть 200"
    response_data = response.json()

    # Проверяем, что ответ содержит сообщение и переданные параметры
    assert response_data.get("message") == "Это ответ на POST-запрос для /example"
    assert response_data.get("received_params") == data


# Тест для несуществующего маршрута
def test_invalid_route():
    url = f"{BASE_URL}/nonexistent"

    response = requests.get(url)

    assert response.status_code == 404, "Статус код должен быть 404"
    assert "error" in response.json(), "Ответ должен содержать ошибку"
