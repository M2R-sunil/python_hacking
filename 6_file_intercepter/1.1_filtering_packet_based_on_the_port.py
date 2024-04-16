#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())## scapu.IP  this is converting ip packets.
    if scapy_packet.haslayer(scapy.Raw): ## this is a print the raw data.
        
      if scapy_packet[scapy.TCP].dport == 80: ## this is aaccess tcp destination port.
        print("scapy request")  
        print(scapy_packet.show())  
      elif scapy_packet[scapy.TCP].sport == 80:
        print("http response")    
        print(scapy_packet.show())
        
      
      
    packet.accept()
queue = netfilterqueue.NetfilterQueue 
queue.bind(0,process_packet) 
    