import os
import socket
import subprocess
from datetime import datetime

print("=" * 50)
print("   AASHMA'S SECURITY AUDIT TOOL v1.0")
print("   Date: " + str(datetime.now()))
print("=" * 50)

#Section 1 - System Info
print("\n[+] SYSTEM INFORMATION")
print("-" * 30)
os.system("whoami")
os.system("hostname")
os.system("uname -a")

#Section 2 - Network Info
print("\n[+] NETWORKINFORMATION ")
print("-" * 30)
os.system("ip addr | grep inet")

#Section 3 - Open Ports
print("\n[+] OPEN PORTS SCAN")
print("-" * 30)
target = "localhost"
common_ports = [21, 22, 23, 25, 80, 443, 445, 3306, 8080, 631]
for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        print("[OPEN] PORT " + str(port))
    else:
        print("[CLOSED] PORT " + str(port))
    sock.close()

#Section 4 - Users
print("\n[+] SYSTEM USERS")
print("-" * 30)
os.system("cat /etc/passwd | cut -d: -f1")

#Section 5 - SUID Files
print("\n[+] SUID FILES CHECK")
print("-" * 30)
os.system("find / -perm -4000 2>/dev/null")

#Section 6 - Running Services
print("\n[+] RUNNING SERVICES")
print("-" * 30)
os.system("ss -tulpn | grep LISTEN")
print("\n" + "=" * 50)
print("   AUDIT COMPLETE!")
print("=" * 50)
