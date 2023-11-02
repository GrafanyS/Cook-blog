<h2 align="center">Cook blog</h2>

### Описание проекта:
##### Блог шеф-повара с рецептами. 
Реализовано:
- профиль пользователя;
- лайки/дизлайки;
- комментарии;
- поиск постов с пагинацией;
- фильтрация постов с помощью django-filters с пагинацией;
- понравившиеся посты;
- чат пользователей с помощью channels;
- удобная админ-панель.


### Инструменты разработки

**Стек:**
- Python >= 3;
- Django >= 3;
- sqlite3;
- Пакеты из файла requirements.txt;

### Разработка

##### 1) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 2) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение

##### 4) Устанавливить зависимости:

    pip install -r requirements.txt

##### 5) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 6) Создать суперпользователя

    python manage.py createsuperuser
    
##### 7) Запустить сервер

    python manage.py runserver


Copyright (c) 2023-present, Valetov Andrei



