.DEFAULT_GOAL := run

build:
	@python setup.py sdist bdist_wheel

check: build
	@twine check dist dist/*

run:
	@python main.py

test:
	@pytest
	@flake8 . --exclude venv,main.py