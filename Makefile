test:
	poetry run pytest

reset-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	rm db.sqlite3
	poetry run python manage.py makemigrations
