DevOps Linux File Creation and Permissions Lab

Task 1: Create Files
touch devops.txt
Creates an empty file.
echo "This is my DevOps notes" > notes.txt
Creates a file and writes content.
vim script.sh
Then add:
echo "Hello DevOps"
Save with ESC :wq
Verify using:
ls -l

Task 2: Read Files
cat notes.txt
Displays file content.
vim -R script.sh
Opens in read-only mode.
head -5 /etc/passwd
Shows first 5 lines.
tail -5 /etc/passwd
Shows last 5 lines.

Task 3: Understand Permissions
ls -l
Example:
-rw-r--r--
Owner: rwGroup: r--
Others: r--
Values:
r = 4
w = 2
x = 1

Task 4: Modify Permissions
chmod +x script.sh
Makes script executable.
chmod 444 devops.txt
Makes read-only.
chmod 640 notes.txt
Owner rw, group r, others none.
mkdir project
chmod 755 project

Task 5: Test Permissions
echo "test" > devops.txt
Will show permission denied.
chmod -x script.sh
./script.sh
Will show permission denied.
Important Permission Numbers
777 = rwx rwx rwx
755 = rwx r-x r-x
644 = rw- r-- r--
640 = rw- r-- ---
444 = r-- r-- r--
