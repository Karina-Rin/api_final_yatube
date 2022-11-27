# API_FINAL_YATUBE
API_final_yatube - это API для cоциальной сети Yatube, в которой пользователи 
могут публиковать посты, просматривать посты других пользователей, оставлять 
комментарии, а также имеется возможность подписаться на интересного автора.

## Технологии

- Python 3.7.9
- Django 2.2
- Django REST Framework
- Библиотеки Djoser и Simple JWT
- Swagger
- Postman

## О проекте

Для взаимодействия с ресурсами описаны и настроены следующие эндпоинты:
- `api/v1/api-token-auth/` (POST): передаём логин и пароль, получаем токен.
- `api/v1/posts/` (GET, POST): получаем список всех постов или создаём новый 
пост.
- `api/v1/posts/{post_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем 
или удаляем пост по id.
- `api/v1/groups/` (GET): получаем список всех групп.
- `api/v1/groups/{group_id}/` (GET): получаем информацию о группе по id.
- `api/v1/posts/{post_id}/comments/` (GET, POST): получаем список всех 
комментариев поста с id=post_id или создаём новый, указав id поста, который 
хотим прокомментировать.
- `api/v1/posts/{post_id}/comments/{comment_id}/` (GET, PUT, PATCH, DELETE): 
получаем, редактируем или удаляем комментарий по id у поста с id=post_id.

### Запускаем проект:

Клонируем репозиторий:

```
git clone https://github.com/Karina-Rin/api_final_yatube.git
```
Переходим в него в командной строке:
```
cd api_final_yatube
```

Cоздаем и активируем виртуальное окружение:

```
python -m venv env
source env/bin/activate
```

Устанавливаем зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполняем миграции:

```
python manage.py migrate
```

Запускаем проект:

```
python manage.py runserver
```

### Примеры запросов

- POST http://127.0.0.1:8000/api/v1/api-token-auth/
Запрос:
```
{
    "username": "onee_user",
    "password": "12345ohH"
}
```
Результат:
```
{
    "email": "",
    "username": "onee_user",
    "id": 1
}
```

- POST http://127.0.0.1:8000/api/v1/posts/

```
{
    "text": "Тут какой-то новый текст",
    "group": 1
}
```

Результат:

```
{
    "id": 1,
    "author": "onee_user",
    "text": "Тут какой-то новый текст",
    "pub_date": "2022-11-27T20:09:12.331905Z",
    "image": null,
    "group": 1
}
```

- GET http://127.0.0.1:8000/api/v1/groups/1/
Результат:
```
{
    "id": 1,
    "title": "Группа 1",
    "slug": "test",
    "description": "Описание группы"
}
```

- POST http://127.0.0.1:8000/api/v1/posts/1/comments/

Запрос:
```
{
    "text": "Весьма интересный пост. Буду ждать еще",
}
```
Результат:
```
{
    "id": 1,
    "author": "onee_user",
    "post": 1,
    "text": "Весьма интересный пост. Буду ждать еще",
    "created": "2022-11-27T20:09:12.331905Z"
}
```

### Документация
```
http://127.0.0.1:8000/redoc/
```
