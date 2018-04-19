SHELL := /bin/bash

init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

isort:
	./venv.sh isort --apply --recursive sheep tests

test_flake8:
	@echo "----> Checking flake8..."
	@./venv.sh flake8 .

test_isort:
	@echo "----> Checking imports..."
	@./venv.sh isort --check-only --quiet --recursive sheep tests || ( \
		echo 'run `make isort` to fix' && exit 1 \
	)

test_mypy:
	@echo "----> Running typechecks..."
	@./venv.sh mypy .

test_unit:
	@echo "----> Running unit tests..."
	@./venv.sh ./test_unit.sh

test: test_flake8 test_isort test_mypy test_unit
