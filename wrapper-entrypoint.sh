#!/bin/bash
set -e

if [ -n "$1" ]; then
    pip install "$1"
    shift
fi

exec /app/entrypoint.sh "$@"