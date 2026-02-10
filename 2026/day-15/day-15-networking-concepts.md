DNS, IP, CIDR & Ports
-----------------------------------------
# 1. How DNS Resolves Names to IPs
- DNS works like a phonebook for the internet.
- It converts names (google.com) into IP addresses.
- Steps: Your system asks DNS -> DNS replies with an IP -> Your system connects.
# 2. IP Addressing Basics (IPv4, Public vs Private)
- IP is like a house number for your device.
- Private IP is used inside your network.
- Public IP is used on the internet.
- Private IP ranges: 10.x.x.x, 172.16-31.x.x, 192.168.x.x
# 3. CIDR & Subnetting (Simple)
- CIDR looks like: 192.168.1.0/24
- "/24" shows network size.
- Bigger number = smaller network.
- Smaller number = bigger network.
- /24 → 256 IPs, /16 → 65k IPs, /32 → 1 IP.
# 4. Common Ports & Their Use
- 22 SSH → remote login
- 80 HTTP → normal websites
- 443 HTTPS → secure websites
- 53 DNS → name resolution
- 3306 MySQL → database
- 5432 PostgreSQL → database
Short Summary: DNS finds IPs, IP identifies devices, CIDR defines network size, Ports define services.
