#!/bin/bash

#function defination
greet() {

echo "Hello, $1!"
}

#function call with argument $1
greet arvind

add() {

read -p "Enter num one :" first
read -p "Enter num two :" second

sum=$(( $first + $second ))

echo "sum of two numbers $sum"
}
add
