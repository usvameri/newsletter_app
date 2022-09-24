# Newsletter App

Newsletter app is a simple app that written with Django uses PostgreSQL as database.

### Requirements:
- asgiref==3.5.2
- backports.zoneinfo==0.2.1
- Django==4.1.1
- Pillow==9.2.0
- psycopg2==2.9.3
- sqlparse==0.4.3
- django-crum==0.7.9
- POSTGRESQL
### Commands
- `python3 manage.py createsuperuser` to create superuser (Required to create newsletter)
- `python3 manage.py makemigrations` to create migrations
- `python3 manage.py migrate` to apply migrations
- `python3 manage.py runserver` to run server

### Notes
- Only **superuser** can create newsletter
- You can change database settings in `newsletter_app/settings.py`
- **Before run the server** Create database with name `newsletterdb` or change database name in `newsletter_app/settings.py`  
- **Before run the server** Create superuser to create newsletter
- **Before run the server** Create migrations and apply migrations
- **Before run the server** Create virtualenvironment and install requirements
- Run the server inside newsletter_app directory (**Server will run on port 8000**)
