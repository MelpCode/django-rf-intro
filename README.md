# Django REST Framework Introduction

### Steps to run the application

1. Clone the application

```
  git clone https://github.com/MelpCode/django-rf-intro.git
```

2. Create virtual environment within the project

```
  python -m virtualenv venv
```

3. Install packages

```
  pip install -r requirements.txt
```

4. Create an ```.env``` file and set

````SECRET_KEY```

5. Execute migrations

```
  python manage.py makemigrations
```

```
  python manage.py migrate
```

6. Start the application

```
  python manage.py runserver
```

