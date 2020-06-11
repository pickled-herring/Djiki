DJANGO=manage.py
CC=python3.7 $(DJANGO)
APP=djiki

run:
	$(CC) runserver

migrate: $(APP)/models.py
	$(CC) makemigrations $(APP)
	$(CC) migrate

static:
	$(CC) collectstatic

test: $(APP)/tests.py
	$(CC) test $(APP)

all: migrate
