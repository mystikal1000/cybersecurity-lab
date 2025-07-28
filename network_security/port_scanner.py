import socket

def scan_ports(host, start=1, end=1024):
    print(f"Scanning {host} from port {start} to {end}")
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open")

# Example:
# scan_ports("127.0.0.1")
