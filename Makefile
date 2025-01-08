# Define the project name
PROJECT_NAME := primes-python

.DEFAULT_GOAL := help

# Show this help message
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
	    helpMessage = match(lastLine, /^# (.*)/); \
	    if (helpMessage) { \
	        helpCommand = $$1; sub(/:$$/, "", helpCommand); \
	        printf "  %-20s %s\n", helpCommand, substr(lastLine, RSTART + 2, RLENGTH - 2); \
	    } \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)
	@echo ""
.PHONY: help


# Install dependencies
install:
	pipenv install --dev
.PHONY: install


# Format all source and test code
format:
	pipenv run black primes/ tests/
.PHONY: format


# Lint-check all code
lint:
	pipenv run flake8 primes/ tests/
.PHONY: lint


# Test all code
test: lint
	pipenv run pytest
.PHONY: test


# Create and serve documentation
docs:
	pipenv run mkdocs serve
.PHONY: docs


# Remove most work product files
clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache .mypy_cache .coverage htmlcov
.PHONY: clean

# Remove all work product files, including .venv
clean-all: clean
	rm -rf .venv
.PHONY: clean
