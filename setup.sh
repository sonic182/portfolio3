#!/bin/bash

PYTHON='./env/bin/python'

case $1 in
"run")
echo "gulp watch starts a django dev server"
# $PYTHON manage.py runserver & gulp watch && fg
gulp watch
;;
"migrate")
$PYTHON manage.py makemigrations
$PYTHON manage.py migrate
;;
esac
