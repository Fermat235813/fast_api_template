#!/usr/bin/env bash

set -e
set -x

coverage run --source=app -m pytest
coverage report --show-missing

## Generates an HTML-representation of test-cases
# coverage html --title "${@-coverage}"