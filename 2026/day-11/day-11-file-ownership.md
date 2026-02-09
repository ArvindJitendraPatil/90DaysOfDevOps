Hint :
Most chown/chgrp operations need sudo
Use -R flag for recursive directory changes
Always verify with ls -l after changes
User must exist before using in chown
Group must exist before using in chgrp/chown

Task 1:
ubuntu@ip-172-31-45-91:/$ ls
bin                boot  etc   lib                lib64       media  opt   root  sbin                snap  sys  usr
bin.usr-is-merged  dev   home  lib.usr-is-merged  lost+found  mnt    proc  run   sbin.usr-is-merged  srv   tmp  var
ubuntu@ip-172-31-45-91:/$  cd home
ubuntu@ip-172-31-45-91:/home$ ls
berlin  nairobi  professor  tokyo  ubuntu
ubuntu@ip-172-31-45-91:/home$ sudo ls -ld
drwxr-xr-x 7 root root 4096 Feb  9 13:25 .
ubuntu@ip-172-31-45-91:/home$ sudo ls -ld /home
drwxr-xr-x 7 root root 4096 Feb  9 13:25 /home
ubuntu@ip-172-31-45-91:/home$ sudo ls -ld /home/*
drwxr-x--- 2 berlin    berlin    4096 Feb  9 13:11 /home/berlin
drwxr-x--- 2 nairobi   nairobi   4096 Feb  9 13:34 /home/nairobi
drwxr-x--- 2 professor professor 4096 Feb  9 12:32 /home/professor
drwxr-x--- 2 tokyo     tokyo     4096 Feb  9 13:10 /home/tokyo
drwxr-x--- 5 ubuntu    ubuntu    4096 Feb  9 11:38 /home/ubuntu

owner : The owner is the main user who controls a file.
group : the group is a set of users who share common access to it.

Task 2: 
ubuntu@ip-172-31-45-91:~$ ls -l devops-file.txt
-rw-rw-r-- 1 ubuntu ubuntu 0 Feb  9 14:27 devops-file.txt
ubuntu@ip-172-31-45-91:~$ sudo chown tokyo devops-file.txt
ubuntu@ip-172-31-45-91:~$ ls -l devops-file.txt
-rw-rw-r-- 1 tokyo ubuntu 0 Feb  9 14:27 devops-file.txt
ubuntu@ip-172-31-45-91:~$ sudo chown berlin devops-file.txt
ubuntu@ip-172-31-45-91:~$ ls -l devops-file.txt
-rw-rw-r-- 1 berlin ubuntu 0 Feb  9 14:27 devops-file.txt

Task 3: 
ubuntu@ip-172-31-45-91:~$ touch team-notes.txt
ubuntu@ip-172-31-45-91:~$ ls -l team-notes.txt
-rw-rw-r-- 1 ubuntu ubuntu 0 Feb  9 14:30 team-notes.txt
ubuntu@ip-172-31-45-91:~$ sudo groupadd heist-team
ubuntu@ip-172-31-45-91:~$ tail -3 /etc/group
nairobi:x:1006:
project-team:x:1007:nairobi,tokyo
heist-team:x:1008:
ubuntu@ip-172-31-45-91:~$ sudo chgrp heist-team team-notes.txt
ubuntu@ip-172-31-45-91:~$ ls -l team-notes.txt
-rw-rw-r-- 1 ubuntu heist-team 0 Feb  9 14:30 team-notes.txt

Task 4: Using chown you can change both owner and group together

ubuntu@ip-172-31-45-91:~$ ls
app-logs   check_package.sh  devops-file.txt  hello.sh  package.sh           rancho.sh  team-notes.txt
chatur.sh  condition.sh      filecheck.sh     num.sh    project-config.yaml  revnum.sh  user_details.sh
ubuntu@ip-172-31-45-91:~$ ls -ld app-logs
drwxr-xr-x 2 root root 4096 Feb  9 14:40 app-logs
ubuntu@ip-172-31-45-91:~$ sudo chown berlin:heist-team app-logs/
ubuntu@ip-172-31-45-91:~$ ls -ld app-logs
drwxr-xr-x 2 berlin heist-team 4096 Feb  9 14:40 app-logs
ubuntu@ip-172-31-45-91:~$ ls -l project-config.yaml
-rw-rw-r-- 1 professor heist-team 0 Feb  9 14:34 project-config.yaml

Task 5:
ubuntu@ip-172-31-45-91:~$ cd heist-project
ubuntu@ip-172-31-45-91:~/heist-project$ ls
plans  vault
ubuntu@ip-172-31-45-91:~/heist-project$ cd plans
ubuntu@ip-172-31-45-91:~/heist-project/plans$ ls
strategy.conf
ubuntu@ip-172-31-45-91:~/heist-project/plans$ sudo groupadd planners
ubuntu@ip-172-31-45-91:~/heist-project/plans$ tail -1 /etc/group
planners:x:1009:
ubuntu@ip-172-31-45-91:~/heist-project/plans$ cd
ubuntu@ip-172-31-45-91:~$ sudo chown -R professor:planners heist-project/
ubuntu@ip-172-31-45-91:~$ ls -ld heist-project/
drwxrwxr-x 4 professor planners 4096 Feb  9 14:49 heist-project/
ubuntu@ip-172-31-45-91:~$ ls -lR heist-project/
heist-project/:
total 8
drwxrwxr-x 2 professor planners 4096 Feb  9 14:49 plans
drwxrwxr-x 2 professor planners 4096 Feb  9 14:49 vault

heist-project/plans:
total 0
-rw-rw-r-- 1 professor planners 0 Feb  9 14:49 strategy.conf

heist-project/vault:
total 0
-rw-rw-r-- 1 professor planners 0 Feb  9 14:52 gold.txt

Task 6:
ubuntu@ip-172-31-45-91:~/bank-heist$ sudo ls -l
total 0
-rw-r--r-- 1 tokyo   vault-team 0 Feb  9 15:06 access-codes.txt
-rw-r--r-- 1 berlin  tech-team  0 Feb  9 15:06 blueprints.pdf
-rw-r--r-- 1 nairobi vault-team 0 Feb  9 15:06 escape-plan.txt
ubuntu@ip-172-31-45-91:~/bank-heist$



