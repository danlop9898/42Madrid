.PHONY: install run debug clean lint lint-strict build test

PYTHON := python3
PIP := $(PYTHON) -m pip

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) a_maze_ing.py config.txt

debug:
	$(PYTHON) -m pdb a_maze_ing.py config.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + || true
	find . -name "*.pyc" -delete || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + || true
	find . -type d -name "dist" -exec rm -rf {} + || true



lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores \
		--ignore-missing-imports --disallow-untyped-defs \
		--check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

build:
	$(PYTHON) -m build

test:
	pytest tests/ -v