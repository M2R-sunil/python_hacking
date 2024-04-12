#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy

## iptables -I OUTPUT -j NFQUEUE queue-num 0 ## this is a use for iptables for modified routing. in host machine in target.
#iptables -I INPUT -j NFQUEUE queue-num 0 ## this is a two chain for forwarding packets. this is a redirect the input and output chain.
# ping -c 1 www.bing.com ## this is a send one request in bing.com
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())## scapu.IP  this is converting ip packets.
    if scapy_packey.haslayer(scapy.DNSRR): ### this is a a filter DNS requests..
        
      print(scapy_packet.show()) ## .get_payload() is showing up a acctual comte of packet.
    packet.accept()
queue = netfilterqueue.NetfilterQueue 
queue.bind(0,process_packet) 
    