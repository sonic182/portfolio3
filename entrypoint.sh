#!/bin/bash

uwsgi --http :8000 --module portfolio3.wsgi --logto /app/log/uwsgi.log
# python manage.py runserver 0.0.0.0:8000
