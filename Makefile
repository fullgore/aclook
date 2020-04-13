PROJECT=aclook
PYTEST_ARGS?=
PYTEST=pytest
FLAKE8_ARGS?=
FLAKE8=flake8

# potentially define env vars that you don't want to be committed to GIT
-include .env.mk

all: app-run

clean:
	find . -name '*.pyc' -exec rm --force {} ;
	find . -name '*.pyo' -exec rm --force {} ;
	name '*~' -exec rm --force  {}

app-lint:
	cd app && env FLASK_ENV=testing $(FLAKE8) --ignore=E501,E999 --exclude migrations,tests $(FLAKE8_ARGS)

app-run:
	cd app && env FLASK_ENV=development gunicorn -w 4 wsgi:app -b 0.0.0.0:8179

app-tests:
	cd app && env FLASK_ENV=testing $(PYTEST) $(PYTEST_ARGS)

.PHONY: all app-lint app-run app-tests
