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

def ping_sweep():
    global ip_list
    global host_count

    # Create a list of all addresses in the network (excluding network and broadcast addresses)
    all_hosts = list(ip_list)
    all_hosts.remove(ip_list.network_address)
    all_hosts.remove(ip_list.broadcast_address)

    # Send ICMP request to each host on the list and check their status
    for host in all_hosts:
        response = sr1(IP(dst=str(host)) / ICMP(), timeout=1, verbose=0)

        if response is None:
            print(f"Host {host} is down or unresponsive.")
        elif int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
            print(f"Host {host} is actively blocking ICMP traffic.")
        else:
            print(f"Host {host} is responding.")
            # Creates counter of live hosts
            host_count += 1

    print(f"Total hosts online: {host_count}")

def main():
    global ip_list
    global host_count

    while True:
        print("Tool Menu:")
        print("1. ICMP Ping Sweep")
        print("2. TCP Port Range Scanner")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # ICMP Ping Sweep mode
            network = input("Enter network address in CIDR notation (e.g., x.x.x.x/24): ")
            ip_list = ipaddress.IPv4Network(network)
            host_count = 0
            ping_sweep()

        elif choice == "2":
            # TCP Port Range Scanner mode
            host = input("Enter the target hostname or IP address: ")
            port_range_str = input("Enter the port range (e.g., 20-80): ")
            start_port, end_port = map(int, port_range_str.split("-"))
            port_range = range(start_port, end_port + 1)
            for port in port_range:
                scan_port(host, port)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()