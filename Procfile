web: gunicorn BankApp.wsgi --log-file -
web: chmod 777 /home/astha/banks/static
web: python manage.py collectstatic --noinput
web: python manage.py collectstatic --noinput; gunicorn BankApp.wsgi:application --bind=0.0.0.0:$PORT

