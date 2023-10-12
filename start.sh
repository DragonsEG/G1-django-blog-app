python manage.py makemigrations --bo-input
python manage.py migrate --no-input

python manage.py loaddata ./data.json

python manage.py runserver 0.0.0.0:8000