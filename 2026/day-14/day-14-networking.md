# Task 1: OSI vs TCP/IP Mapping
- OSI has 7 layers, TCP/IP has 4.
- Top 3 OSI layers = TCP/IP Application layer,Presention and Session layer
- Transport layer = same in both.
- Network layer = Internet layer.
- Data Link + Physical = Network Access.
# Task 2: Essential Connectivity Commands
- ping <host> # Check if host is reachable
- traceroute <host> # Check path
- nc -zv <IP> <port> # Check if port is open
- nslookup <domain> # DNS check
- ip a # Check your IP
- ss -tulnp # Check open ports
# Task 3: Mini Network Check
1. ping <target>
2. nc -zv <target> <port>
3. nslookup <domain>
4. traceroute <target>
------------------------------------------------------------------------------------------------------------------------------------
# OSI vs TCP/IP (Simple)
- OSI has 7 layers (L1–L7). TCP/IP has 4 layers.
- Top 3 OSI layers = TCP/IP Application layer.
- Bottom 2 OSI layers = TCP/IP Link layer.
# Where Common Protocols Sit
- IP → Internet layer (routing, addressing).
- TCP/UDP → Transport layer (ports, delivery).
- HTTP/HTTPS → Application layer (web traffic).
- DNS → Application layer (name to IP lookup).
# Real Example
curl https://example.com
- curl = Application layer tool.
- HTTPS = Application layer.
- Uses TCP = Transport layer.
- Travels over IP = Internet layer.
- Uses Ethernet/Wi-Fi = Link layer.
Short form: App → TCP → IP → Link

Hands-on Network Checklist
-------------------------------------------
# 1. Identity Check
Command: hostname -I
Observation: Shows your IP address. Example: 192.168.1.20
# 2. Reachability Test
Command: ping <target>
Observation: Check latency (ms) and packet loss. Example: 32ms, 0% loss.
# 3. Path Check
Command: traceroute <target>
Observation: Note long hops/timeouts. Example: hop 7 slow, hop 10 timeout.
# 4. Port Check
Command: ss -tulpn
Observation: Shows listening services. Example: sshd listening on port 22.
# 5. DNS Resolution
Command: nslookup <domain>
Observation: Shows resolved IP. Example: google.com -> 142.250.183.206
# 6. HTTP Header Check
Command: curl -I <url>
Observation: Shows HTTP status. Example: 200 OK.
# 7. Connection Snapshot
Command: netstat -an | head
Observation: Count LISTEN vs ESTABLISHED. Example: 5 ESTABLISHED, 3 LISTEN.
-------------------------------------------------------------------------------------------------------------------------
# 1. Identify a Listening Port
Command:
ss -tulpn
Example Observation:
SSH is listening on port 22.
# 2. Test the Port from the Same Machine
Command:
nc -zv localhost 22
OR (for web ports):
curl -I http://localhost:22
Example Observation:
Connection succeeded.
# 3. One-line Result
Port 22 is reachable.
If NOT reachable, next checks:
- systemctl status sshd (check service)
- sudo ufw status (check firewall)

Quick Incident Response:
-----------------------------------------------
# 1. Fastest Signal When Something Is Broken
- The fastest command is usually: ping <target>
- If it stops replying or shows packet loss, something is wrong immediately.
# 2. What Layer to Check Next
- If DNS fails: Check Application layer DNS -> then Network layer (IP reachability).
- If HTTP 500 shows: Check Application layer first (web server/app issue), not network.
# 3. Two Follow-up Checks in a Real Incident
- Check service logs: journalctl -u <service> -n 50
- Check port status: ss -tulpn | grep <port>
