mig:
	python manage.py makemigrations
	python manage.py migrate

fr:
	pip freeze -> requirements.txt

run:
	python manage.py runserver

sur:
	python manage.py createsuperuser