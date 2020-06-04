DJANGO=manage.py
CC=python3.7 $(DJANGO)
APP=djiki

run:
	$(CC) runserver

migrate: $(APP)/models.py
	$(CC) makemigrations $(APP)
	$(CC) migrate

test: $(APP)/tests.py
	$(CC) test $(APP)

all: migrate
