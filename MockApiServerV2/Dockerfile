# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Копируем только необходимые файлы
COPY requirements.txt .
COPY src/mock_server.py src/
COPY config/config.json config/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт
EXPOSE 8000

# Запускаем сервер
ENV FLASK_APP=src/mock_server.py
ENV FLASK_ENV=production
CMD ["python", "src/mock_server.py"]