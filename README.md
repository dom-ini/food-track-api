# Food Track
[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![pl](https://img.shields.io/badge/lang-pl-white.svg)](README.pl.md)

## Project description

Detailed information about this project are included in [the front-end repository](https://github.com/dom-ini/food-track-front/).

## Links

### Front-end repository
https://github.com/dom-ini/food-track-front/

## Tech stack

- Python 3.10
- Django 4.2
- Celery
- PostgreSQL 15
- Docker

## Getting started

In the project directory, create _.env_ file and add the required values (you can see _.env.example_ file for reference).

Run `docker-compose up` to run the development server.

In the _ft-web_ container terminal, run `python manage.py migrate` to apply migrations to the database.

To create a superuser, run `python manage.py createsuperuser`. You can access the admin console at http://localhost:8000/admin.

Access the API documentation at http://localhost:8000/api/v1 or http://localhost:8000/api/v1/docs.
