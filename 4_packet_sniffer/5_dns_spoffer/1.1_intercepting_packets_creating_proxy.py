#!/usr/bin/env python

import netfilterqueue


## iptables -I FORWARD -j NFQUEUE queue-num 0 ## this is a use for iptables for modified routing.
## pip install netfilterqueue ## this is a install Kali and capture the data.
def process_packet(packet):
    print(packet)
    packet.accept()# .drop this is a drop the all packets he is block the internet. ## this is forward the packets.
queue = netfilterqueue.NetfilterQueue ## this is a netfilter module.
queue.bind(0,process_packet) ## process_packet is a call back function execute the binded queue

# iptables flush ## this is a flush the all table.