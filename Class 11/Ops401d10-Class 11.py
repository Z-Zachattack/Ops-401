#!/usr/bin/env python3 

# Script Name:                  Class 11
# Author:                       Zachariah Woodbridge
# Date of latest revision:      22 Jan 2024
# Purpose:                      Creates a TCP Port Range Scanner that tests whether a TCP port is open or closed.
# Disclaimer:                   This script was written with the assistance of codeium.

# Declaration of imports
import scapy.all as scapy
from scapy.all import sr1, IP, TCP, send

# Declaration of variables

# Declaration of functions
def scan_port(host, port):
    """
    Scans the specified port on the given host to determine its state (open, closed, or filtered).

    Args:
    - host (str): The target host IP address.
    - port (int): The port number to be scanned.

    Returns:
    - None
    """

    # Set a source port
    src_port = 22
    
    # Send a TCP SYN packet and wait for a response
    response = sr1(IP(dst=host) / TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)

    # Analyze the response and print the state of the port
    if response is None:
        print(f"Port {port} is filtered (silently dropped).")
    elif response.haslayer(TCP):
        tcp_layer = response.getlayer(TCP)
        if tcp_layer.flags == 0x12:
            send(IP(dst=host) / TCP(sport=src_port, dport=port, flags="R"), verbose=0)
            print(f"Port {port} is open.")
        elif tcp_layer.flags == 0x14:
            print(f"Port {port} is closed.")
    else:
        print(f"Port {port} is in an unknown state.")

# Main function
def main():
    target_host = "scanme.nmap.org"
    port_range = range(20, 23)

    # Sends a single ping and prints out the response packet
    response = sr1(IP(dst=target_host) / scapy.ICMP(), verbose=0)
    if response:
        response.show()

    # Calls scan function on all ports in the range
    for port in port_range:
        scan_port(target_host, port)

if __name__ == "__main__":
    main()