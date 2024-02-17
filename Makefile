.DEFAULT_GOAL := all

bandit:
	poetry run bandit -r . -x ./static
toml_sort:
	poetry run toml-sort pyproject.toml --all --in-place
flake8:
	poetry run flake8 .
isort:
	poetry run isort .
pylint:
	poetry run pylint . --recursive=y --load-plugins pylint_django --django-settings-module=food_track.settings
black:
	poetry run black .
mypy:
	poetry run mypy --install-types --non-interactive .
test:
	poetry run pytest tests
lint: black flake8 isort pylint mypy toml_sort
