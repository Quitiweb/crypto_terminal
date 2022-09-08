SHELL := /bin/bash

install:
	python -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt
	source .venv/bin/activate && pre-commit install

start_django_server:
	source .venv/bin/activate && cd crypto_terminal && python manage.py runserver

init_database:
	source .venv/bin/activate && cd crypto_terminal && python manage.py migrate
	source .venv/bin/activate && cd crypto_terminal && DJANGO_SUPERUSER_PASSWORD=admin python manage.py createsuperuser --noinput --username admin --email admin@admin.com
	make load_data

load_data:
	source .venv/bin/activate && cd crypto_terminal && python manage.py load_coin_data
