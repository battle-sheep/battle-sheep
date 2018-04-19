#!/bin/bash
set -e
if [[ $PIPENV_ACTIVE != "1" ]]; then
  exec pipenv shell "$@"
else
  exec "$@"
fi
