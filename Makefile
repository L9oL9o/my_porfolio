mig:
	python manage.py makemigrations
	python manage.py migrate

rq:
	pip freeze -> requirements.txt

run:
	python manage.py runserver