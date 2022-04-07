# api_yatube
api_yatube
Проект api_yatube предназначен для создания эндпойнтов приложения yatude.

Автор Василий  -  студент Яндекс Практикума.

Язык программирования: Python

Используемые библиотеки и пакеты:
    django               2.2.16
    djangorestframework  3.12.4
    pytest               6.2.4
    pytest-django        4.4.0
    pytest-pythonpath    0.7.3
    requests             2.26.0
    Pillow               8.3.1
    sorl-thumbnail       12.7.0

Установка приложения:

git clone <http или ssh из репозитория>

python -m venv venv

source venv/Scripts/activate

Установка зависимостей:

pip install -r requirements.txt

Запуск приложения из директории api_yatube, содержащей файл manage.py:

python manage.py runserver

В проекте предусмотрен весь спектр основных CRUD запросов с различным уровнем разрешения.

Примеры запросов и ответов на них для авторизованных пользователей:

GET   api/v1/posts/  -  в ответе вернет список постов

GET   api/v1/posts/1/comments/1/  -  в ответе вернет объект первого 
                                     комментария первого поста

POST  api/v1/posts/ - создаст новый пост, если данные в запросе валидны

POST  api/v1/groups/ - вернет ошибку 405, т.к. создание группы через 
                                     api не доступно.