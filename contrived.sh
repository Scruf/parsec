#!/bin/bash
source parsec/bin/activate
pip install -r requirements.txt
export EGORS_TEST_BACUP=$1
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 127.0.0.1:$2
