VENV = /home/adrolc/venvs/DSA_Linux
BIN = $(VENV)/bin
PYTHON = $(BIN)/python3
PIP = $(BIN)/pip

.PHONY: install
install:
	$(PIP) install -r requirements.txt

.PHONY: install_dev
install_dev:
	$(PIP) install -r requirements_dev.txt

.PHONY: typehint
typehint:
	$(BIN)/mypy --ignore-missing-imports src/

.PHONY: test
test:
	$(PYTHON) -m unittest discover -v -s tests/

.PHONY: lint
lint:
	$(BIN)/pylint src/

.PHONY: checklist
checklist: lint typehint test

.PHONY: black
black:
	$(BIN)/black -l 79 src/
	$(BIN)/black -l 99 tests/

.PHONY: clean
clean:
	find . -type f -name "*.pyc" | xargs rm -fr
	find . -type d -name __pycache__ | xargs rm -fr