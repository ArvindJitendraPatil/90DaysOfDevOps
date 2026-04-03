#!/bin/bash

#!/bin/bash

# Function to check disk usage
check_disk() {
    echo "Disk Usage:"
    df -h /
}

# Function to check memory usage
check_memory() {
    echo "Memory Usage:"
    free -h
}

# Main section
check_disk
check_memory
