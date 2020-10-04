
setup: 
	#source .skills/bin/activate
	python3 -m venv .skills

install: 
	pip install --upgrade pip && \
	pip install -r requirements.txt

test: 
	python3 -m pytest -vv --cov=skills tests/*.py

lint: 
	pylint --disable=R,C,W1203 skills.py
	hadolint Dockerfile

all: install lint test
