#!/bin/bash
echo "Makemigrationszzzzzzzzzzz"
python manage.py makemigrations
echo "##################################"

echo "Migratezzzzzzzzzzz"
python manage.py migrate
echo "##################################"

echo "Runserverzzzzzzzzzz"
python manage.py runserver 0.0.0.0:8000