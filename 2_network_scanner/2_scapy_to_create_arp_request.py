#!/usr/bin/env python

import scapy.all as scapy

def scan(ip): # this is a define a scapy function
    arp_request = scapy.ARP(pdst=ip) # scapy.ARP() this is print the summary this is a scapy function # this is a module for scapy. #(pdst=ip) this is second mathod printing the ip address.
    #arp_request.pdst=ip # this is first mathod # this is a print the whois ip 192.168.62.2/24. basically this is two mathod of printing this ip.
    print(arp_request.summary()) # this is a print summary for data
    #scapy.ls(scapy.ARP()) # this is first step. # scapy.ls this function showing all list details.
    # and last scapy.ls(scapy.ARP()) # comment this object. no need the printing list.
    
scan("192.169.62.2/24")   
    