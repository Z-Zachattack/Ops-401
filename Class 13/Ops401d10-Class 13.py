# Script Name:                  Class 13
# Author:                       Zachariah Woodbridge
# Date of latest revision:      24 Jan 2024
# Purpose:                      Python script that pings an IP address determined by the user; If the host exists, scan its ports and determine if any are open.
# Disclaimer:                   This script was written with the assistance of codeium.

# Declaration of imports
import scapy.all as scapy
from scapy.all import ICMP, IP, sr1, TCP, send

# Declaration of variables

# Declaration of functions
# Ping Sweeper
def ping():
    target_ip = input("Enter the target IP address: ")

    # Perform ICMP ping sweep
    response = sr1(IP(dst=target_ip) / ICMP(), timeout=1, verbose=0)

    if response is None:
        print(f"Host {target_ip} is down or unresponsive.")
    elif int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
        print(f"Host {target_ip} is actively blocking ICMP traffic.")
    else:
        print(f"Host {target_ip} is responsive, beginning port scan...")
        # Call port scan function
        port_scan(target_ip)

# Function to prompt user for port range and call port scan function
def port_scan(host):
    port_range_str = input("Enter the port range (e.g., 20-80): ")
    start_port, end_port = map(int, port_range_str.split("-"))
    port_range = range(start_port, end_port + 1)
    print("Scanning Common Ports...")

    for port in port_range:
        scan_port(host, port)
# Port Scanner
def scan_port(host, port):
    src_port = 22  # Replace with your desired source port
    response = sr1(IP(dst=host) / TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)

    if response is None:
        print(f"Port {port} is filtered.")
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:
            send(IP(dst=host) / TCP(sport=src_port, dport=port, flags="R"), verbose=0)
            print(f"Port {port} is open.")
        elif response.getlayer(TCP).flags == 0x14:
            print(f"Port {port} is closed.")
    else:
        print(f"Port {port} is in an unknown state.")

# Main 
if __name__ == "__main__":
    ping()

# End
