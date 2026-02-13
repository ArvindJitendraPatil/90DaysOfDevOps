shebag : shebag is used for scrpit feature run.feacture like sh,bash,csh,zsh.
What happens if you remove the shebang line?
if we not used shebag in script they will used default /bin/sh and if we use bash fecature in sh. they will getting error.

Challenge Tasks:
Task 1:
ubuntu@ip-172-31-40-21:~$ ./hello.sh
Hello, DevOps!
ubuntu@ip-172-31-40-21:~$ cat hello.sh
#!/bin/bash
echo "Hello, DevOps!"

Task 2: Variables
ubuntu@ip-172-31-40-21:~$ cat variables.sh
#!/bin/bash
Name="ARVIND"
Ram='Amol'
ROLE="DevOps Engineer"
echo "Hello, I am $Name,$Ram and I am a $ROLE"
ubuntu@ip-172-31-40-21:~$ sh variables.sh
Hello, I am ARVIND,Amol and I am a DevOps Engineer
Try using single quotes vs double quotes — what's the difference?
we use both for decalre the variable value.

Task 3: User Input with read
ubuntu@ip-172-31-40-21:~$ ./greet.sh
Enter the fav. tooldocker
My fav. tool is docker
ubuntu@ip-172-31-40-21:~$ cat greet.sh
#!/bin/bash
read -p "Enter the fav. tool" name
echo "My fav. tool is $name"

Task 4: If-Else Conditions 1)check_number.sh
ubuntu@ip-172-31-40-21:~$ ./check_number.sh
Enter the number :5
positive
ubuntu@ip-172-31-40-21:~$ ./check_number.sh
Enter the number :-6
negative
ubuntu@ip-172-31-40-21:~$ ./check_number.sh
Enter the number :0
Zero
ubuntu@ip-172-31-40-21:~$ cat check_number.sh
#!/bin/bash
read -p "Enter the number :" number
if [ $number -gt 0 ]; then
        echo "positive"
elif [ $number -lt 0 ]; then
        echo "negative"
elif [ $number -eq 0 ]; then
        echo "Zero"
fi

2) file_check.sh
ubuntu@ip-172-31-40-21:~$ ./file_check.sh
Enter the filenamevariable.sh
file does not exist
ubuntu@ip-172-31-40-21:~$ ls
check_number.sh  file_check.sh  greet.sh  hello.sh  variables.sh
ubuntu@ip-172-31-40-21:~$ ./file_check.sh
Enter the filenamegreet.sh
file is exist
#!/bin/bash
read -p "Enter the filename" filename
if [ -f $filename ]; then
        echo "file is exist"
else
        echo "file does not exist"
fi

Task 5: Combine It All
ubuntu@ip-172-31-40-21:~$ ./server_check.sh
Enter the service name :sshd
Do you want to check the sshd istatus? (y/n)y
Unit sshd.service could not be found.
sshd is NOT active
ubuntu@ip-172-31-40-21:~$ cat server_check.sh
#!/bin/bash

read -p "Enter the service name :" service_name
read -p "Do you want to check the $service_name istatus? (y/n)" ans

if [ "$ans" = "y" ]; then
    if sudo systemctl status "$service_name"; then
        echo "$service_name is ACTIVE"
    else
        echo "$service_name is NOT active"
    fi
else
    echo "Skipped."
fi


















































