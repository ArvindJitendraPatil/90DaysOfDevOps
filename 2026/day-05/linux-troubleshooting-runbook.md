 Linux Troubleshooting Commands
1. CPU Check:
 top
2. Memory Check:
 free -h
3. Disk Check:
 df -h
4. Network Check:
 ss -tulpn
5. Logs Check:
 journalctl -xe
 tail -f /var/log/syslog

Target Service: ssh (OpenSSH Server)
1. Environment Basics:
 uname -a → Kernel OK, system stable.
 cat /etc/os-release → OS info loads correctly.
2. Filesystem Sanity:
 mkdir /tmp/runbook-demo; cp /etc/hosts /tmp/runbook-demo/hosts-copy → FS writable.
 ls -l /tmp/runbook-demo → Permissions normal.
3. CPU & Memory Snapshot:
 top → CPU normal, no spikes.
 free -h → Memory usage healthy, swap minimal.
4. Disk & IO:
 df -h → Disk usage acceptable.
 du -sh /var/log → Log directory size normal.
5. Network:
 ss -tulpn → sshd listening on port 22.
 ping 8.8.8.8 → Connectivity stable.
6. Logs Reviewed:
 journalctl -u ssh -n 50 → No critical errors.
 tail -n 50 /var/log/auth.log → Normal login activity.
7. Quick Findings:
 System healthy overall.
 No CPU, memory, disk, or network bottlenecks detected.
 SSH service responding normally.
8. If This Worsens – Next Steps:
 1. Restart ssh: systemctl restart ssh.
 2. Increase logging: set LogLevel VERBOSE in sshd_config.
 3. Collect diagnostics: strace -p $(pidof sshd).
