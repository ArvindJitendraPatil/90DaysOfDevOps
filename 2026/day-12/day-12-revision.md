# Process Check Commands
- ps aux
- top
- htop
# Service Check Commands
- systemctl status <service>
- journalctl -u <service> -n 50
- systemctl restart <service>
# File Permission Change Commands
- chmod 755 <file>
- chown user:group <file>
- ls -l
--------------------------------------------------------------------------------------------------------------------
1. Three commands that save me the most time and why:
 - top: Helps me quickly see CPU, RAM, and which process is using more resources.
 - systemctl status <service>: Shows me if a service is running or failed in seconds.
 - journalctl -u <service>: Gives me fast logs for troubleshooting without searching everywhere.
2. How I check if a service is healthy (first 2–3 commands):
 - systemctl status <service>
 - journalctl -u <service> -n 50
 - ss -tulnp | grep <port>
3. Safe way to change ownership and permissions:
 Example:
 sudo chown appuser:appgroup /var/www/app && sudo chmod 750 /var/www/app
 This keeps the right owner and gives limited but safe access.
4. What I will improve in the next 3 days:
 - Better troubleshooting speed using logs and monitoring.
 - Automating repeated tasks with shell scripts.
 - Improving my understanding of permissions and security basics.
--------------------------------------------------------------------------------------------------------------------------------------------
1. echo >> (Append text)
 echo "Hello world" >> file.txt
 echo "New content" > file.txt
2. chmod (Change permissions)
 chmod 755 script.sh
 chmod +x script.sh
 chmod -w file.txt
3. chown (Change ownership)
 sudo chown arvind file.txt
 sudo chown arvind:developers file.txt
 sudo chown -R arvind:developers /opt/myapp
4. ls -l (List files with details)
 ls -l
 ls -la
5. cp (Copy files/directories)
 cp source.txt destination.txt
 cp -r /path/src /path/dest
 cp -i file1 file2  -- why use -i? To avoid accidental overwrite of important files.
6. mkdir (Create directory)
 mkdir new_folder
 mkdir -p /opt/myapp/logs  --  -p → create parent directories as needed
rm -ri old_backup -- The -i asks confirmation before deleting each file.
