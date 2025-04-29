User Links API
Описание
User Links API — сервис для управления пользователями, ссылками и коллекциями. Позволяет пользователям регистрироваться, входить в систему, сохранять ссылки и группировать их в коллекции.
Функциональность
- Регистрация и аутентификация (Djoser, JWT)
- Управление ссылками (создание, редактирование, удаление)
- Группировка ссылок в коллекции
- Генерация превью ссылок с Open Graph
- Swagger API-документация (drf-yasg)
- Админ-панель Django для управления данными
- Docker-контейнеры для удобного развертывания
- GitHub для совместной работы и контроля версий


Установка проекта
1. Клонирование репозитория
git clone (https://github.com/AndreiParmon/user_links.git)
cd user_links

2. Установка зависимостей
pip install -r requirements.txt

3. Для заполнения базы данных тестовыми данными необходимо выполнить файл populate_db.py, который расположен в корне проекта.  

4. Настройка базы данных
python manage.py migrate

5. Создание суперпользователя
python manage.py createsuperuser

6. Запуск сервера
python manage.py runserver

   
Запуск в Docker
1. Создание и запуск контейнеров
docker-compose up --build -d

2. Применение миграций
docker-compose exec web python manage.py migrate

3. Создание суперпользователя
docker-compose exec web python manage.py createsuperuser

4. Заполнение базы тестовыми данными
docker-compose exec web python populate_db.py

   
API Документация
После запуска сервер доступен по:
- Swagger: http://127.0.0.1:8000/swagger/
- Админ-панель: http://127.0.0.1:8000/admin/


Использование API

Регистрация пользователя:
POST /auth/users/

Тело запроса:
{
    "username": "testuser",
    "password": "password123",
    "email": "test@example.com"
}


Авторизация (получение токена):
POST /auth/token/login/


Тело запроса:
{
    "username": "testuser",
    "password": "password123"
}


Ответ:
{
    "auth_token": "your_token_here"
}



Остановка и удаление контейнеров
docker-compose down.
Эта команда остановит все контейнеры.
