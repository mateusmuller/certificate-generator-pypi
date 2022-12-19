.DEFAULT_GOAL := run

run:
	@python main.py

test:
	@pytest
	@flake8 . --exclude venv