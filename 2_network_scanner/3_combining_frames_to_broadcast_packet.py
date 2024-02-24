#!/usr/bin/env python

import scapy.all as scapy

def scan(ip): # this is a define a scapy function
    arp_request = scapy.ARP(pdst=ip) # scapy.ARP() this is print the summary this is a scapy function # this is a module for scapy. #(pdst=ip) this is second mathod printing the ip address.
    arp_request.show() # this is showing details information about each packets.
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff::ff") # this is a module for scapy for mac address destination to broadcast mac scapy.Ether() # this is set to  destination to broadcast mac.
    broadcast.show()
    #broadcast.dst="ff:ff:ff:ff:ff::ff"
    #scapy.ls(scapy.Ether()) # this is showing list mac address.
    #print(broadcast.summary()) # this is print the broadcast variable values.
    arp_request_broadcast = broadcast/arp_request # this is / forward slash combine print the packets value. 
    arp_request.show()
    #print(arp_request_broadcast.summary()) # no need this print statement for after adding the .show() module.
    
    
      
scan("192.169.62.2/24")   
    