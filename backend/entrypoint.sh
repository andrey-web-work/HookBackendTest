#! /bin/sh

python manage.py migrate
python manage.py collectstatic --noinput --clear

python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL

gunicorn backend.wsgi:application -b dj:8000