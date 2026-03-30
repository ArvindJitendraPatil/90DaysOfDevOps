# Challenge Tasks:
# Task 1: For Loop
- 1)Create for_loop.sh that:
- Loops through a list of 5 fruits and prints each one
<img width="500" height="750" alt="fruits_for_loop" src="https://github.com/user-attachments/assets/3347f40b-7ed4-432c-a61f-2972a4ec5308" />

- 2)Create count.sh that:
- Prints numbers 1 to 10 using a for loop
<img width="747" height="656" alt="count_for_loop" src="https://github.com/user-attachments/assets/1beff971-d741-4f49-ae77-4cacbde3e250" />

## Task 2: While Loop
1. Create `countdown.sh` that:
   - Takes a number from the user
   - Counts down to 0 using a while loop
   - Prints "Done!" at the end
<img width="677" height="747" alt="count_while_loop" src="https://github.com/user-attachments/assets/9baa1d9a-bcfd-4a0d-9366-24f9e34db168" />

## Task 3: Command-Line Arguments
1. Create `greet.sh` that:
   - Accepts a name as `$1`
   - Prints `Hello, <name>!`
   - If no argument is passed, prints "Usage: ./greet.sh <name>"

<img width="700" height="543" alt="greet sh" src="https://github.com/user-attachments/assets/b66978e1-3797-4a7d-ba81-48f62c7e5e46" />

2. Create `args_demo.sh` that:
   - Prints total number of arguments (`$#`)
   - Prints all arguments (`$@`)
   - Prints the script name (`$0`)

<img width="861" height="331" alt="args" src="https://github.com/user-attachments/assets/c49d0ae2-ad37-4c37-8181-85f529433a42" />

## Task 4: Install Packages via Script
1. Create `install_packages.sh` that:
   - Defines a list of packages: `nginx`, `curl`, `wget`
   - Loops through the list
   - Checks if each package is installed (use `dpkg -s` or `rpm -q`)
   - Installs it if missing, skips if already present
   - Prints status for each package

#!/bin/bash

package=("nginx" "curl" "wget")


for pkg in "${package[@]}";do
	dpkg -s $pkg &>/dev/null || { echo "$pkg installing..."; apt install $pkg -y 1>/dev/null; }
done

for pkg in "${package[@]}";do
	 dpkg -s $pkg &>/dev/null && echo " STATUS - $pkg is INSTALLED " || echo " STATUS - $pkg is NOT INSTALLED "
done



























## What I learned

* Using loops(while,for)
* Error handling
* Using CLI arguments




