# Погружение в Django

## Установка окружения

### Склонируйте проект «Погружение в Django» в папку _Dev/_.

Должна получиться такая структура:

```
Dev/
└── jump_into_django/
    ├── acme_project/
    │   ├── acme_project/
    │   │   ├── __init__.py
    │   │   ├── asgi.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── catalog/
    │   │   ├── __init__.py
    │   │   ├── apps.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── homepage/
    │   │   ├── __init__.py
    │   │   ├── apps.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── templates/
    │   │   ├── catalog/
    │   │   │   ├── product_detail.html
    │   │   │   └── product_list.html
    │   │   ├── homepage/
    │   │   │   └── index.html
    │   │   ├── includes/
    │   │   │   ├── footer.html
    │   │   │   └── header.html
    │   │   └── base.html
    │   └── manage.py
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    └── setup.cfg
```

### Создайте виртуальное окружение

1. Запустите редактор Visual Studio Code и через меню «_Файл» / «Открыть папку»_ откройте папку _Dev/jump_into_django/_.
2. Запустите терминал в VS Code, удостоверьтесь, что вы работаете из директории _jump_into_django/_ (если вы работаете под Windows, убедитесь, что в терминале запущен Git Bash, а не PowerShell или что-нибудь ещё), и выполните команду:

- Linux/macOS

  ```bash
  python3 -m venv venv
  ```

- Windows

  ```python
  python -m venv venv
  ```

В директории _jump_into_django/_ будет развёрнуто виртуальное окружение и появится папка `venv`, в которой будут храниться все зависимости проекта, а структура файлов станет такой:

```
Dev/
└── jump_into_django/
    ├── acme_project/
    ├── venv/
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    └── setup.cfg
```

### Активация виртуального окружения

в терминале перейдите в корневую директорию проекта _Dev/jump_into_django/_ и выполните команду:

- Linux/macOS

  ```bash
  source venv/bin/activate
  ```

- Windows

  ```bash
  source venv/Scripts/activate
  ```

Теперь все команды в терминале будут предваряться строкой `(venv)`.

💡 Все дальнейшие команды в терминале надо выполнять с активированным виртуальным окружением.

Обновите pip:

```bash
python -m pip install --upgrade pip
```

### Установка зависимостей из файла _requirements.txt_:

Находясь в папке _Dev/jump_into_django/_, выполните команду:

```bash
pip install -r requirements.txt
```

### Создай файл `.env`

В корне проекта _Dev/jump_into_django/_ создай файл `.env`.

Например:

```env
SECRET_KEY=<ваш_секретный_ключ_сюда>
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### Применение миграций

Перейдите в директорию _Dev/jump_into_django/acme_project/_ и выполните команду:

```bash
python manage.py migrate
```

### Запуск проекта в dev-режиме

Перейдите в директорию _Dev/jump_into_django/acme_project/_ и выполните команду:

```bash
python manage.py runserver
```

В ответ Django сообщит, что сервер запущен и проект доступен по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
