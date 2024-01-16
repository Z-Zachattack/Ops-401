#!/usr/bin/env python3

# Script Name:                  Class 02
# Author:                       Zachariah Woodbridge
# Date of latest revision:      06 Jan 2024
# Purpose:                      Python script that is an uptime counter
# Disclaimer:                   This script was created with the assistance of ChatGPT

# Declaration of imports
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ping3 import ping

# Declaration of variables

# Declaration of functions
def notify(email, password, subject, body):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, f"Subject: {subject}\n\n{body}")

def uptime_sensor(ping_target, email, password):
    previous_status = None

    while True:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        success = ping(ping_target, timeout=1)
        current_status = "ICMP Active, continue attack" if success else "ICMP Inactive, it's probably a Windows computer so attack anyways"

        if previous_status and previous_status != current_status:
            subject = "Host Status Change Notification"
            body = f"Status changed from {previous_status} to {current_status} at {timestamp} for target {ping_target}"
            notify(email, password, subject, body)

        print(f"{timestamp} {current_status} to {ping_target}")
        
        previous_status = current_status
        time.sleep(2)

# Main
if __name__ == "__main__":
    ping_target = input("Who is your target? -e.g. 8.8.8.8 ")  # Replace with the desired IP address
    email = input("Enter your email address: ") # user email address	
    password = input("Enter your email password: ") # user password

    uptime_sensor(ping_target, email, password)
# End
