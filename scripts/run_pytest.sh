#!/usr/bin/bash

# This script is used to run the test suite for the MPT application.
# It is intended to be run from the root directory of the project.

docker compose run mpt_app poetry run pytest