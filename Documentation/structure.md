## Django Project Structure

![Django Project Structure](/Documentation/assets/structure.png)

After running (`django-admin startproject 'project_name'`):
```bash
|__project_name
  |__ __init__.py
  |__ settings.py
  |__ urls.py
  |__ wsgi.py
  |__ asgi.py
|__ manage.py

```

* `__init__.py`: This is an empty file. The function of this file is to tell the Python interpreter that this directory is a package.

* `settings.py`: It contains the Django project configuration:
    - contains several variable names, and if you change the value, your application will work accordingly.
    - contains sqlite3 as the default database. We can change this database to Mysql, PostgreSQL, or MongoDB according to the web application we create.
    - contains some pre-installed apps and middleware that are there to provide basic functionality.
* `urls.py`: it contains all the endpoints that we should have for our website. This file tells Django that if a user comes with this URL, direct them to that particular website or image whatsoever it is.
* `wsgi.py`: WSGI stands for Web Server Gateway Interface, it describes the way how servers interact with the applications.
* `asgi.py`: ASGI works similar to WSGI but comes with some additional functionality.  ASGI stands for Asynchronous Server Gateway Interface. It is now replacing its predecessor WSGI.
* `manage.py`: This file is used as a command-line utility for our projects. We will use this file for debugging, deploying, and running our web applications.

    The main `manage.py` commands are:
    - `runserver`: This command is used to start the test server for our web application, provided by the Django framework.
    - `makemigrations`: we use this command to apply new migrations across projects and apps that have been carried out due to the changes in the database.
    - `migrate` This is the prior step of the makemigration command. We use this for making the changes to the modules in the database. 


After running (`python anage.py startapp 'app_name'`):
```bash
|__app_name
    |__ migrations
        |__ __init__.py
    |__ __init__.py
    |__ admin.py
    |__ apps.py
    |__ models.py
    |__ tests.py
    |__ views.py

```