install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py

format:
	black *.py

test:
	python -m pytest -vv ../tests/test_app.py

deploy:
	echo "Deploying app"

all: install lint test deploy