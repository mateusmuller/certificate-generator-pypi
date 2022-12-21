.DEFAULT_GOAL := run

build:
	@python setup.py sdist bdist_wheel

check: build
	@twine check dist/*

push: check
	@twine upload -r testpypi dist/* --verbose --skip-existing

clean:
	@rm -rf dist *.egg-info build

run:
	@python main.py

test:
	@black .
	@bandit -r tests -s B101,B105
	@bandit -r certgenerator
	@pytest
	@flake8 . --exclude venv,main.py