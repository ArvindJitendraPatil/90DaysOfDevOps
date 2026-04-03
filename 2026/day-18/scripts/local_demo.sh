#!/bin/bash
local_func() {
  local x=10
  echo "Inside local_func: x=$x"
}

global_func() {
  y=20
  echo "Inside global_func: y=$y"
}

# Calls
local_func
echo "Outside local_func: x=$x"   # x is not accessible

global_func
echo "Outside global_func: y=$y" # y leaks outside
