#!/usr/bin/env python

import scapy.all as scapy

def scan(ip): # this is a define a scapy function
    scapy.arping(ip)
scan("192.169.62.2/24")   
