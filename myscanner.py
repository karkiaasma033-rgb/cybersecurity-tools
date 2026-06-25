import socket
target = "localhost"
print("Scanning ",  target)
for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN!")
    s.close()
print("Scan complete!")
