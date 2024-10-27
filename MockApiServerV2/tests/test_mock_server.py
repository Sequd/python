# tests/test_mock_server.py
import unittest
import requests
import time



class TestMockAPI(unittest.TestCase):
    """Тесты Mock API сервера с использованием реальных HTTP запросов."""
    # Базовый URL для локального сервера
    base_url = "http://localhost:8000"

    def test_get_user(self):
        """Тест GET запроса для получения информации о пользователе."""
        response = requests.get(f"{self.base_url}/api/users", params={"id": "123"})

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], "123")
        self.assertEqual(data["name"], "John Doe")
        self.assertIn("email", data)

    def test_post_user(self):
        """Тест POST запроса для создания пользователя."""
        response = requests.post(
            f"{self.base_url}/api/users",
            json={"id": "456"}
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], "456")
        self.assertIn("name", data)
        self.assertIn("email", data)

    def test_get_products(self):
        """Тест GET запроса для получения списка продуктов."""
        response = requests.get(
            f"{self.base_url}/api/products",
            params={"category": "electronics"}
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["category"], "electronics")
        self.assertIn("products", data)
        self.assertTrue(isinstance(data["products"], list))

    def test_missing_required_params(self):
        """Тест запроса с отсутствующими обязательными параметрами."""
        response = requests.get(f"{self.base_url}/api/users")

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn("error", data)
        self.assertIn("Missing required parameters", data["error"])

    def test_method_not_allowed(self):
        """Тест запроса с неразрешенным HTTP методом."""
        response = requests.put(f"{self.base_url}/api/users", json={"id": "789"})

        self.assertEqual(response.status_code, 405)

    def test_invalid_endpoint(self):
        """Тест запроса к несуществующему endpoint."""
        response = requests.get(f"{self.base_url}/api/invalid")

        self.assertEqual(response.status_code, 404)

    def test_invalid_json(self):
        """Тест POST запроса с невалидным JSON."""
        response = requests.post(
            f"{self.base_url}/api/users",
            data="invalid json",
            headers={"Content-Type": "application/json"}
        )

        self.assertEqual(response.status_code, 400)

    # def test_server_response_time(self):
    #     """Тест времени отклика сервера."""
    #     start_time = time.time()
    #     requests.get(f"{self.base_url}/api/users", params={"id": "123"})
    #     response_time = time.time() - start_time
    #
    #     self.assertLess(response_time, 1.0)  # Ответ должен прийти менее чем за 1 секунду


if __name__ == '__main__':
    unittest.main()