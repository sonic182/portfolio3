#!/bin/bash

PYTHON='./env/bin/python'

case $1 in
"run")
$PYTHON manage.py runserver
;;
"migrate")
$PYTHON manage.py makemigrations
$PYTHON manage.py migrate
;;
esac
