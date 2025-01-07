# Define the project name
PROJECT_NAME := primes

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

# Format all source and test code
format:
	pipenv run black primes/ tests/

# Lint-check all code
lint:
	pipenv run flake8 primes/ tests/

# Test all code
test:
	make lint
	pipenv run pytest

# Create and serve documentation
docs:
	pipenv run mkdocs serve
