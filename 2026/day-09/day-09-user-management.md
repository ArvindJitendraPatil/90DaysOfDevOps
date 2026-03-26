# Linux User & Group Management Practice

## Task 1
sudo useradd -m tokyo && sudo useradd -m berlin && sudo useradd -m professor && ls && tail -5 /etc/passwd  

## Task 2
sudo groupadd developers && sudo groupadd admins && tail -5 /etc/group  

## Task 3
sudo usermod -aG developers tokyo && sudo usermod -aG admins berlin && sudo usermod -aG developers berlin && sudo usermod -aG admins professor && tail -5 /etc/group  

**Output:** tokyo:x:1001: | berlin:x:1002: | professor:x:1003: | developers:x:1004:tokyo,berlin | admins:x:1005:berlin,professor  

## Task 4
ls -ld /opt/dev-project && sudo chgrp developers /opt/dev-project && ls -ld /opt/dev-project && sudo chmod 755 /opt/dev-project && ls -ld /opt/dev-project  

**Output:** drwxr-xr-x 2 root developers 4096 Feb 9 12:52 /opt/dev-project  

### Switch Users
sudo su - tokyo && whoami && touch f1.txt && echo "this is first file" >> f1.txt && cat f1.txt && exit  
sudo su - berlin && whoami && touch f2.txt && echo "this is my second user file" >> f2.txt && cat f2.txt  

## Task 5
sudo usermod -aG project-team nairobi && sudo usermod -aG project-team tokyo && tail -6 /etc/group  

**Output:** berlin:x:1002: | professor:x:1003: | developers:x:1004:tokyo,berlin | admins:x:1005:berlin,professor | nairobi:x:1006: | project-team:x:1007:nairobi,tokyo  

### Team Workspace
sudo mkdir /opt/team-workspace && sudo chgrp project-team /opt/team-workspace && ls -ld /opt/team-workspace && sudo chmod 755 /opt/team-workspace && ls -ld /opt/team-workspace  

**Output:** drwxr-xr-x 2 root project-team 4096 Feb 9 13:28 /opt/team-workspace  

### Nairobi User
sudo su - nairobi && whoami && touch f3.txt && echo "this is my third file" >> f3.txt && cat f3.txt  

**Output:** this is my third file  

---
- Users: tokyo, berlin, professor, nairobi  
- Groups: developers, admins, project-team  
- Directories: `/opt/dev-project` (developers), `/opt/team-workspace` (project-team)  
- Files: tokyo → f1.txt, berlin → f2.txt, nairobi → f3.txt

## What I Learned

* Gained a clear understanding of how users and groups work in Linux.
* Practiced managing permissions and observed their impact on collaboration.
* Even if two users belong to the same group and share access to a directory, they cannot automatically write to or modify each other’s files. By default, when a user creates a file inside a directory:
  -The file is owned by the user and their primary group (not necessarily the directory’s group).
  -The default file permissions usually give write access only to the owner, while the group gets read access.
  -As a result, other group members can view the file but cannot edit or delete it.
  Example : Shared directory scenario.
* Set up direct login access for newly created users using SSH keys and proper permissions.
