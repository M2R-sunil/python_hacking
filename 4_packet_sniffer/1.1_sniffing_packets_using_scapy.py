#!/usr/bin/env python

import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=packet_sniff) ## this false do not store anything in the computer ## prn this is a call function.
def packet_sniff(snifer):
    print(snifer)
sniff("eth0") ## this is a sniff eth0 interface
