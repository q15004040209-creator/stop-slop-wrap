#!/bin/bash
# stop-slop demo checker (Shell wrapper)
# Requires: python3

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ -z "$1" ]; then
    echo "Usage: bash demo_checker.sh \"Your text here\""
    echo "   or: bash demo_checker.sh --file "
    exit 1
fi

if [ "$1" = "--file" ]; then
    python3 "$SCRIPT_DIR/demo_checker.py" --file "$2"
else
    python3 "$SCRIPT_DIR/demo_checker.py" "$@"
fi