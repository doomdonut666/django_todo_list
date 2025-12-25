# Django TODO list

## Требования и установка

### Требования:
 - Python
 - UV

### Установка:
    Внимание! Инструкция для linux, т.к я использую именно его

  1) Клонируйте репозиторий:
  ```
  git clone git@github.com:doomdonut666/django_todo_list.git
  ```

  2) Перейдите в директорию:
  ```
  cd django_todo_list
  ```

 3) Установите зависимости используя UV:
 ```
 uv sync
 ```

 4) Активируйте виртуальное окружение (venv):
 ```
 source .venv/bin/activate
 ```

 5) Запустите сервер:
 ```
 python manage.py runserver
 ```

 6) Перейдите по ссылке:
 http://127.0.0.1:8000/
