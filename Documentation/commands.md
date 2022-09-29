## Install Django
```bash
pip install django
```
## Run the django server
```bash
python manage.py runserver
```
## Create a new project
```bash
django-admin strartprojet 'project_name'
```

## Create an APP inside django project
```bash
python manage.py startapp 'app_name'
```

## After Adding a model to models.py, Run:
```bash
python manage.py makemigration
```

## Create Database tables
```bash
python manage.py migrate
```

## Create user with admin privileges
```bash
python manage.py createsuperuser
```