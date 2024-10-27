# Используем базовый образ Python
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Открываем порт для доступа к приложению
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "main.py"]
