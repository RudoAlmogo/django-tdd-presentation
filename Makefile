test:
	poetry run pytest

reset-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	rm db.sqlite3
	poetry run python manage.py makemigrations

run-grpc:
	poetry run python manage.py grpcrunaioserver 127.0.0.1:8000

generateproto:
	poetry run python manage.py generateproto
