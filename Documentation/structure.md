## Django Project Structure

![Django Project Structure](/Documentation/assets/structure.png)

After running (`django-admin startproject 'project_name'`)
```bash
|__project_name
|             |__ __init__.py
|             |__ settings.py
|             |__ urls.py
|             |__ wsgi.py
|             |__ asgi.py
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