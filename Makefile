DJANGO=manage.py
CC=python3.7 $(DJANGO)
APP=djiki

migrate: $(APP)/models.py
	$(CC) makemigrations $(APP)
	$(CC) migrate

test: $(APP)/tests.py
	$(CC) test $(APP)

run:
	$(CC) runserver
