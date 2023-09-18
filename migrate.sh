#!/bin/bash
echo "Makemigrations"
python manage.py makemigrations
echo "##################################"

echo "Migrate"
python manage.py migrate
echo "##################################"

echo "Runserver"
python manage.py runserver 0.0.0.0:8000