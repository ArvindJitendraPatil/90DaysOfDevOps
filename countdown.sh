#!/bin/bash
read -p "Enter a number: " n
while [ $n -ge 0 ]; do
  echo $n
  n=$((n-1))
done
echo "Done!"

