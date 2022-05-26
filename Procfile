release: python manage.py migrate
web: gunicorn FoodTrack.wsgi
worker: celery -A FoodTrack worker