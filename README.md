### 🆕 Створення проєкту Django з шаблону

###!!! В проекті розкоментовано .env в .gitignore це зроблено задля коректної роботи проекту з коробки

#### 1\. Клонування репозиторію

Для початку, склонуйте репозиторій із шаблоном собі на комп'ютер:

```bash
git clone https://github.com/KuthikBohdan1/django_celery_template
```

#### 2\. Створення нового проєкту

Перейдіть до каталогу, де ви хочете створити новий проєкт. Потім скористайтеся командою `django-admin startproject`, вказавши шлях до склонованого шаблону:

```bash
django-admin startproject --template=/шлях/до/шаблону назва_проєкту .
```

або якщо ви хочите мати гарну інструкцію

```bash
django-admin startproject   --template=/шлях/до/шаблону   --extension=py,env,md,yml   --name=README.md,.env.example   назва_проєкту .

```


### ⚙️ Підготовка та запуск

#### 1\. Віртуальне середовище

Створіть та активуйте віртуальне середовище для ізоляції залежностей проєкту.

  * **Створення:**
    ```bash
    python -m venv .venv
    ```
  * **Активація:**
      * **Windows:**
        ```bash
        .venv\Scripts\activate
        ```
      * **Linux/macOS:**
        ```bash
        source .venv/bin/activate
        ```

#### 2\. Встановлення залежностей

Встановіть усі необхідні бібліотеки з файлу `requirements.txt`:

```bash
pip install -r requirements.txt
```

#### 3\. Міграції бази даних

Застосуйте міграції для створення необхідних таблиць у базі даних:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 4\. Створення суперкористувача

Створіть адміністратора для доступу до панелі управління Django:

```bash
python manage.py createsuperuser
```

#### 5\. Запуск сервера

Запустіть локальний сервер розробки, щоб перевірити роботу проєкту:

```bash
python manage.py runserver
```


###celery

```bash
  celery -A {{ project_name }} worker -l info
```

or with lib watchfiles > https://pypi.org/project/watchfiles/
```bash
watchfiles "celery -A {{ project_name }} worker -l info" 
```

###flower

```bash
celery -A {{ project_name }} flower -l info port=5555
```
or 
```bash
watchfiles "celery -A {{ project_name }} flower -l info port=5555"
```

```bash
pip install --upgrade pip
```