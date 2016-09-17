#!/bin/sh
echo "Running python manage.py makemigrations"
python manage.py makemigrations
echo "Running python manage.py migrate"
python manage.py migrate
echo "Running python manage.py runserver_plus 0.0.0.0:8000"
python manage.py runserver_plus 0.0.0.0:8000
