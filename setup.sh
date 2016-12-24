#!/bin/bash

PYTHON='./env/bin/python'

case $1 in
"run")
  echo "gulp watch starts a django dev server"
  # $PYTHON manage.py runserver & gulp watch && fg
  gulp watch
  # $PYTHON manage.py runserver
;;
"migrate")
  $PYTHON manage.py makemigrations
  $PYTHON manage.py migrate
;;
"secret")
  python -c 'import random; import string; print("".join([random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)]))'
;;
"vps")
  ssh root@mogollon.com.ve
;;
"push")
  git push bitbucket master
  git push && ssh root@mogollon.com.ve
;;
"pull")
  git pull && sh setup.sh up
;;
"up")
  docker-compose build web && docker-compose up --no-deps -d web
;;
esac
