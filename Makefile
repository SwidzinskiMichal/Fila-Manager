.PHONY: help

help: ## Shows a list of commands with short descriptions
	@grep -E '^[a-zA-Z_-]+:.?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

setup:	## Setup project
	@echo "Setup"

install:	## Installs project requirements
	pip install -r requirements.txt

venv:	## Installs project requirements
	python3 -m venv .venv

test:	## Run tests
	pytest

start:	## Starts Flask server
	@echo "Start"