SHELL := /bin/bash

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

run:
	python manage.py runserver [::]:8000

lint:
	./scripts/run-linters.sh

load:
	python manage.py loaddata ./fixtures/*

test:
	python manage.py test

migration:
	python manage.py makemigrations

fake-migrate:
	python manage.py migrate --fake

migrate:
	python manage.py migrate

migrate-data:
	python -m migration_scripts.main

superuser:
	python manage.py createsuperuser

heroku:
	git push heroku master

deploy:
	docker-compose build
	docker-compose up -d

down:
	docker-compose down
