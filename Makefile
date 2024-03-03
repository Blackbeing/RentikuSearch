.DEFAULT_GOAL := help

PY_SRC := RentikuSearch/ tests/

.PHONY: help
help:  ## Print this help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

.PHONY: all
all: lint checks tests

.PHONY: lint
lint: lint-black lint-isort lint-flake  ## Run linting tools on the code.

.PHONY: lint-black
lint-black:  ## Lint the code using black.
	python -m black --line-length=78 $(PY_SRC) .

.PHONY: lint-isort
lint-isort:  ## Sort the imports using isort.
	python -m isort --line-length=78 $(PY_SRC) .

.PHONY: lint-flake
lint-flake:
	python -m  autoflake -ir --exclude tests/fixtures --remove-all-unused-imports --ignore-init-module-imports $(PY_SRC)

.PHONY: checks
checks: check-types

.PHONY: check-types
check-types: ## Check types
	python -m mypy $(PY_SRC)

.PHONY: tests
tests:
	python -m pytest tests
