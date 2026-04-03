#!/bin/bash
set -euo pipefail

# Undefined variable (triggers error with -u)
#echo "Value: $UNDEF_VAR"

# Command that fails (triggers exit with -e)
#ls /nonexistent/path

# Pipe failure (triggers error with -o pipefail)
cat /nonexistent/file | grep "test"
