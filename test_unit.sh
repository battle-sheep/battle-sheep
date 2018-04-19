#!/bin/bash
set -e

if [ $# -eq 0 ]; then
  args=("tests")
else
  args=("$@")
fi

exec pytest \
  --disable-socket \
  --showlocals \
  "${args[@]}"

