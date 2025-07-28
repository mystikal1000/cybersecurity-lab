import socket

def sniff():
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    print("Sniffing packets... (Press Ctrl+C to stop)")
    while True:
        raw_data, addr = sock.recvfrom(65536)
        print(f"Packet received: {raw_data[:64]}...")

# Requires sudo
# sudo python packet_sniffer.py
