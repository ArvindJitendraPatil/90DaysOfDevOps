#!/bin/bash

echo "Checking application health..."

response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/health)

if [ "$response" -eq 200 ]; then
    echo "Health check passed!"
    exit 0
else
    echo "Health check failed!"
    exit 1
fi
