import socket
import os

print("=" * 40)
print("  AASHMA ' S CYBERSECURITY TOOLKIT")
print("=" * 40)

print("\n[1] Scanning target...")
target = "localhost"
for port in [21, 22, 80, 443, 631, 3306]:
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target , port))
    if result ==0:
        print("Port " + str(port) + " is OPEN!")
    else:
        print("Port " + str(port) + " is closed")
    sock.close()

print("\n[2] System Information:")
os.system("whoiam")
os.system("hostname")

print("\n[3] Scan Complete!")
print("=" * 40)
