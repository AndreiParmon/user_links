#!/bin/sh

echo "Применяем миграции..."
python manage.py migrate

echo "Собираем статику..."
python manage.py collectstatic --noinput

echo "Заполняем тестовыми данными..."
python populate_db.py

echo "Запускаем сервер..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
