# Real time output of commands I practiced

## Process commands
* `ps -aux | head -n 10` - List running processes(top 10 lines).
  <img width="1271" height="403" alt="image" src="https://github.com/user-attachments/assets/4eaaeb2e-8438-4fd9-86c7-3c68aae4ac14" />

* * `pgrep -x sshd` - Get the process id by process name.
  <img width="515" height="147" alt="image" src="https://github.com/user-attachments/assets/92c83e7a-b882-40ea-9f79-584bc430743c" />

## Service commands
* `systemctl status | head -n 20` - Prints first 20 lines of system service status summary.
<img width="710" height="521" alt="image" src="https://github.com/user-attachments/assets/2e19d9fd-92f9-4c6f-8475-84d50a8e75cd" />
* `systemctl list-units --type=service --state=running | head` - Prints first 10 lines of running services status.
<img width="1505" height="361" alt="image" src="https://github.com/user-attachments/assets/800268d2-26de-42a5-8273-f4a25c9cf85b" />

## Log commands
* `journalctl -u ssh` - Displays logs for the SSH service.
<img width="1916" height="418" alt="image" src="https://github.com/user-attachments/assets/5c08da99-1a3c-4fdb-b0d3-abdf6719480d" />

* `sudo tail -n 20 /var/log/auth.log` - Last 20 lines of the authentication log(ssh, sudo).
<img width="1907" height="598" alt="image" src="https://github.com/user-attachments/assets/ed70f70d-dd15-48b6-b97c-2a116a41b2c1" />

## Service for inspection (SSH)
- `systemctl status ssh`

<img width="1905" height="513" alt="image" src="https://github.com/user-attachments/assets/a29ff715-e370-4c18-9bc9-57a4096a4c03" />

- It is running now lets stop it. And try to connect to localhost.

<img width="865" height="687" alt="image" src="https://github.com/user-attachments/assets/7d9ec3c3-92e7-454d-8aea-8d2246118437" />

- Giving error
  
<img width="781" height="148" alt="image" src="https://github.com/user-attachments/assets/e7f31cd3-48ab-4e26-b325-59829f175223" />

- Let's view logs and check

<img width="1905" height="551" alt="image" src="https://github.com/user-attachments/assets/d78c79db-88b0-4ace-bc9a-f9073cbdbfe1" />

- Log shows the service is stopped let's start the ssh service and check again

<img width="1901" height="696" alt="image" src="https://github.com/user-attachments/assets/eb2c658e-74cb-405d-a6c4-4fe28f739559" />

-Service started.
