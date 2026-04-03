#!/bin/bash

# Check if an argument is passed
if [ $# -eq 0 ]; then
  echo "Usage: ./greet.sh <name>"
else
  echo "Hello, $1!"
fi

