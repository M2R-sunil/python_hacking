#!/usr/bin/env python

import scapy.ass as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniff_packet) 
    
def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw): ## haslayer is a function that show all layers. 
           print(packet[scapy.Raw].load)## .load  raw layer of scapy analysis.
         ##print(packet.show()) ## this is a showing all the content of scapy. 
sniff("eth0") 