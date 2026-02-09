Task 1
sudo useradd -m tokyo
sudo useradd -m berlin
sudo useradd -m professor
ls
tail -5 /etc/passwd

Task 2
sudo groupadd developers
sudo groupadd admins
tail -5 /etc/group

Task 3 
ubuntu@ip-172-31-45-91:/opt$ sudo usermod -aG developers tokyo
ubuntu@ip-172-31-45-91:/opt$ sudo usermod -aG admins berlin
ubuntu@ip-172-31-45-91:/opt$ sudo usermod -aG developers berlin
ubuntu@ip-172-31-45-91:/opt$ sudo usermod -aG admins professor
ubuntu@ip-172-31-45-91:/opt$ tail -5 /etc/group
tokyo:x:1001:
berlin:x:1002:
professor:x:1003:
developers:x:1004:tokyo,berlin
admins:x:1005:berlin,professor
Task 4
ubuntu@ip-172-31-45-91:/opt$ ls -ld /opt/dev-project
drwxr-xr-x 2 root root 4096 Feb  9 12:52 /opt/dev-project
ubuntu@ip-172-31-45-91:/opt$ sudo chgrp developers /opt/dev-project
ubuntu@ip-172-31-45-91:/opt$ ls -ld /opt/dev-project
drwxr-xr-x 2 root developers 4096 Feb  9 12:52 /opt/dev-project
ubuntu@ip-172-31-45-91:/opt$ sudo chmod 755 /opt/dev-project
ubuntu@ip-172-31-45-91:/opt$ ls -ld /opt/dev-project
drwxr-xr-x 2 root developers 4096 Feb  9 12:52 /opt/dev-project

sudo -s -- for single line
cd /home/tokyo
ubuntu@ip-172-31-45-91:/home$ sudo su - tokyo
$ whoami
tokyo
$ touch f1.txt
$ ls
f1.txt
$ echo "this is first file" >> f1.txt
$ cat f1.txt
this is first file
$ exit
ubuntu@ip-172-31-45-91:/home$ sudo su - berlin
$ whoami
berlin
$ touch f2.txt
$ ls
f2.txt
$ echo "this is my second user file" >> f2.txt
$ cat f2.txt
this is my second user file
sudo -s
cd /home/tokyo

Task 5: 
ubuntu@ip-172-31-45-91:~$ sudo usermod -aG project-team nairobi
ubuntu@ip-172-31-45-91:~$ sudo usermod -aG project-team tokyo
ubuntu@ip-172-31-45-91:~$ tail -6 /etc/group
berlin:x:1002:
professor:x:1003:
developers:x:1004:tokyo,berlin
admins:x:1005:berlin,professor
nairobi:x:1006:
project-team:x:1007:nairobi,tokyo
ubuntu@ip-172-31-45-91:~$ sudo mkdir /opt/team-workspace
ubuntu@ip-172-31-45-91:~$ sudo chgrp project-team /opt/team-workspace
ubuntu@ip-172-31-45-91:~$ ls -ld /opt/team-workspace
drwxr-xr-x 2 root project-team 4096 Feb  9 13:28 /opt/team-workspace
ubuntu@ip-172-31-45-91:~$ chmod 755 /opt/team-workspace
chmod: changing permissions of '/opt/team-workspace': Operation not permitted
ubuntu@ip-172-31-45-91:~$ sudo chmod 755 /opt/team-workspace
ubuntu@ip-172-31-45-91:~$ ls -ld /opt/team-workspace
drwxr-xr-x 2 root project-team 4096 Feb  9 13:28 /opt/team-workspace
ubuntu@ip-172-31-45-91:~$ sudo useradd -m nairobi
useradd: user 'nairobi' already exists
ubuntu@ip-172-31-45-91:~$ sudo groupadd project-team
groupadd: group 'project-team' already exists
ubuntu@ip-172-31-45-91:~$ sudo su nairobi
$ whoami
nairobi
$ touch f3.txt
touch: cannot touch 'f3.txt': Permission denied
$ vi f3.txt
$ exit
ubuntu@ip-172-31-45-91:~$ sudo su - nairobi
$ whoami
nairobi
$ touch f3.txt
$ echo "this is my third file" >> f3.txt
$ cat f3.txt
this is my third fileask 5 

