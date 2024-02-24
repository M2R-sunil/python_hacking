#!/usr/bin/env python

import scapy.all as scapy

def scan(ip): # this is a define a scapy function
    arp_request = scapy.ARP(pdst=ip) # scapy.ARP() this is print the summary this is a scapy function # this is a module for scapy. #(pdst=ip) this is second mathod printing the ip address.
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff::ff") # this is a module for scapy for mac address destination to broadcast mac scapy.Ether() # this is set to  destination to broadcast mac.
    arp_request_broadcast = broadcast/arp_request # this is / forward slash combine print the packets value. 
    answerd_list, unanswerd_list = scapy.srp(arp_request_broadcast,timeout=1) #.srp() function for scapy he is sending and receiving packets. this srp use for two values answerd and unanswered.
    # timeout function working on time he is keep wating one second and get no response go forwarding. he is not stuck the program.
    print(answerd_list.summary())
    #print(unanswerd.summary())
 
scan("192.169.62.2/24")   
    