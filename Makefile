# Makefile for web scraper project

# Define variables for common paths
VENV_DIR = .venv
PYTHON = poetry run python
SPHINX_BUILD = poetry run sphinx-build
BUILD_DIR = _build/html

# Default target
.PHONY: help
help:
	@echo "Usage:"
	@echo "  make install     - Install dependencies"
	@echo "  make run         - Run the scraper"
	@echo "  make test        - Run the tests"
	@echo "  make build       - Build the package"
	@echo "  make publish     - Publish the package"
	@echo "  make clean       - Clean up the environment and temporary files"
	@echo "  make dev         - Install development dependencies"
	@echo "  make html        - Generate HTML documentation using Sphinx"

# Install dependencies using Poetry
.PHONY: install
install:
	poetry install

# Install development dependencies
.PHONY: dev
dev:
	poetry install --dev

# Run the scraper
.PHONY: run
run:
	poetry run python -m web_scraper

# Run tests using pytest
.PHONY: test
test:
	poetry run pytest

# Build the project package
.PHONY: build
build:
	poetry build

# Publish the project to PyPI
.PHONY: publish
publish:
	poetry publish --build

# Clean up the virtual environment and other temporary files
.PHONY: clean
clean:
	rm -rf $(VENV_DIR) .pytest_cache $(BUILD_DIR)

# Generate HTML documentation using Sphinx
.PHONY: html
html:
	$(SPHINX_BUILD) -b html . $(BUILD_DIR)
	@echo "Documentation generated in $(BUILD_DIR)"
