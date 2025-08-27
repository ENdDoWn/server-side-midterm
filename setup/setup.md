# 🛠️ Setup Instructions for `django`

## pip3 or pip && python3 or python can use both

## if no lib
```bash
pip install virtualenv
```

## 🧪 Create and activate virtual environment

**(Windows)**

```bash
python -m venv .venv
.venv\Scripts\activate
```

***Create project first then install psycop2***
## 📥 Install required packages

```bash
pip install django
```

## setup project

```bash
#create project
django-admin startproject [name]
#create app
python manage.py startapp [name]
```

## install psycop2 after startproject

```bash
pip install psycopg2
OR
pip install psycopg2-binary
```

## setup database and app in file setting

```bash
# Database setting
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "appname",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# Add app to INSTALLED_APPS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Add your apps here
    "name",
]

#set-up static folder
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

## ⚙️ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🚀 Run the development server

```bash
python manage.py runserver
```

Then go to `http://127.0.0.1:8000` in your browser.

---
