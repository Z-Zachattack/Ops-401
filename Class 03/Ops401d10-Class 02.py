#!/usr/bin/env python3

# Script Name:                  Class 02
# Author:                       Zachariah Woodbridge
# Date of latest revision:      09 Jan 2024
# Purpose:                      Python script that detects whether an IP address can be pinged or not
# Disclaimer:                    This script was written with the assistance of codeium.

# Declaration of imports
import time
from ping3 import ping

# Declaration of variables

# Declaration of functions

# This is an uptime sensor function that pings IP addresses.
def uptime_sensor(ping_target):
    while True:
        # This took too long to get the time correct, but its the timestamp in a format
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        # ChatGPT informed me that this would be a good addition
        success = ping(ping_target, timeout=1)

        if success:
            status = "ICMP Active, continue attack"
        else:
            status = "ICMP Inactive, it's probably a Windows computer so attack anyways"

        # Prints the obligatory timestamp
        print(f"{timestamp} {status} to {ping_target}")
        
        # 2-second pause between pings
        time.sleep(2)

# Main
if __name__ == "__main__":
    ping_target = input("Who is your target? -e.g. 8.8.8.8 ")  # Replace with the desired IP address
    uptime_sensor(ping_target)

# End