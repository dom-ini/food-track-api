# Food Track
[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![pl](https://img.shields.io/badge/lang-pl-white.svg)](README.pl.md)

## Opis projektu

Szczegółowe informacje na temat tego projektu znajdują się w [repozytorium front-endowym](https://github.com/dom-ini/food-track-front/).

## Linki

### Repozytorium front-endowe
https://github.com/dom-ini/food-track-front/

## Stack technologiczny

- Python 3.10
- Django 4.2
- Celery
- PostgreSQL 15
- Docker

## Uruchamianie projektu

W katalogu projektu utwórz plik _.env_ i dodaj wymagane wartości (możesz zobaczyć plik _.env.example_ w celach informacyjnych).

Uruchom polecenie `docker-compose up`, aby uruchomić serwer deweloperski.

W terminalu kontenera _ft-web_ uruchom polecenie `python manage.py migrate`, aby zastosować migracje do bazy danych.

Aby utworzyć superużytkownika, uruchom polecenie `python manage.py createsuperuser`. Dostęp do konsoli administratora można uzyskać pod adresem http://localhost:8000/admin.

Dostęp do dokumentacji API można uzyskać pod adresem http://localhost:8000/api/v1 lub http://localhost:8000/api/v1/docs.
