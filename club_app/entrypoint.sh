cd /app

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput

python3 manage.py custom_createsuperuser --username admin --password admin

uwsgi --ini uwsgi.ini