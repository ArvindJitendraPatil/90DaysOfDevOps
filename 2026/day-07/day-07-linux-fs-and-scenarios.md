Scenario 1: Service 'myapp' Not Starting
1. systemctl status myapp → Check whether active/failed.
2. journalctl -u myapp -n 50 → Review recent errors.
3. systemctl is-enabled myapp → Confirm boot startup.
4. ls -l /etc/myapp/ → Check config permissions.
Scenario 2: High CPU Usage
1. top → Real-time CPU view.
2. ps aux --sort=-%cpu | head → Top CPU-consuming processes.
3. pidstat 1 → CPU usage per process.
4. systemctl status <service> → Check affected services.
Scenario 3: Finding Docker Logs
1. systemctl status docker → Check state.
2. journalctl -u docker -n 50 → View last logs.
3. journalctl -u docker -f → Follow logs live.
Scenario 4: Script Permission Issue
1. ls -l /home/user/backup.sh → Identify missing execute bit.
2. chmod +x /home/user/backup.sh → Add execute permission.
3. ls -l /home/user/backup.sh → Verify correct permissions.
4. ./backup.sh → Execute script.
