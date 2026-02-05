1. Check Running Processes:
The 'ps -ef' command shows ALL running processes on Linux in full format.
Columns Meaning:
UID - User running the process
PID - Process ID
PPID - Parent Process ID
C - CPU usage percentage
STIME- Start time of the process
TTY - Terminal associated with process
TIME - Total CPU time used
CMD - The actual command executed
Example Output:
UID PID PPID C STIME TTY TIME CMD
root 1 0 0 10:20 ? 00:00:03 /sbin/init
root 512 1 0 10:20 ? 00:00:00 /usr/sbin/sshd
root 920 512 0 10:25 ? 00:00:00 sshd: user@pts/0
user 921 920 0 10:25 pts/0 00:00:00 -bash
user 1200 921 1 10:26 pts/0 00:00:00 python app.py
user 1300 921 0 10:27 pts/0 00:00:00 ps -ef

e → show every process
f → show in full format.
ps aux - shows running processes
top - shows live CPU/process view
pgrep ssh - shows ssh process ID

2. Inspect One Systemd Service (ssh):
systemctl status ssh - check service status
systemctl restart ssh - restart service

3. Check Logs:
journalctl -u ssh - logs for ssh service
tail -n 50 /var/log/syslog - last 50 log lines

4. Mini Troubleshooting Flow:
1. systemctl status ssh
2. pgrep ssh
3. journalctl -u ssh
4. systemctl restart ssh
5. ss -tulnp | grep ssh
