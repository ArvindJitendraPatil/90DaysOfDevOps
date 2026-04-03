#!/bin/bash
set -euo pipefail

print_host_os() {
  echo "=== Hostname & OS ==="
  echo "Hostname: $(hostname)"
  echo "OS Info: $(uname -a)"
}

print_uptime() {
  echo "=== Uptime ==="
  uptime
}

print_disk_usage() {
  echo "=== Disk Usage (Top 5) ==="
  df -h | sort -k3 -r | head -n 5
}

print_memory_usage() {
  echo "=== Memory Usage ==="
  free -h
}

print_top_cpu() {
  echo "=== Top 5 CPU Processes ==="
  ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6
}

main() {
  print_host_os
  print_uptime
  print_disk_usage
  print_memory_usage
  print_top_cpu
}

main
