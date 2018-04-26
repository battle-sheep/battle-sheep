SHELL := /bin/bash

init:
	@echo "---> Installing pipenv..."
	@pip install pipenv --upgrade
	@echo "---> Installing Python packages..."
	@pipenv install --dev

isort:
	@echo "---> Sorting imports..."
	@pipenv run isort --apply --quiet --recursive sheep tests

test_flake8:
	@echo "----> Checking flake8..."
	@pipenv run flake8 .

test_isort:
	@echo "----> Checking imports..."
	@pipenv run isort --check-only --quiet --recursive sheep tests || ( \
		echo 'run `make isort` to fix' && exit 1 \
	)

test_mypy:
	@echo "----> Running typechecks..."
	@pipenv run mypy .

test_unit:
	@echo "----> Running unit tests..."
	@pipenv run ./test_unit.sh

test: test_flake8 test_isort test_mypy test_unit
