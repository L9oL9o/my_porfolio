mig:
	python manage.py makemigrations
	python manage.py migrate

rq:
	pip freeze -> requirements.txt

run:
	python manage.py runserver

sur:
	python manage.py createsuperuser

git:
	git status
	git add .
	git commit
	git push