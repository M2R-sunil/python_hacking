#!/usr/bin/env python

import scapy.all as scapy

def scan(ip): # this is a define a scapy function
    arp_request = scapy.ARP(pdst=ip) # scapy.ARP() this is print the summary this is a scapy function # this is a module for scapy. #(pdst=ip) this is second mathod printing the ip address.
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff::ff") # this is a module for scapy for mac address destination to broadcast mac scapy.Ether() # this is set to  destination to broadcast mac.
    arp_request_broadcast = broadcast/arp_request # this is / forward slash combine print the packets value. 
    answerd_list = scapy.srp(arp_request_broadcast,timeout=1)[0] # This is the print the result answerd_list element [0] # element 0 using for the answerd_list
  
    #print(answerd_list.summary()) # because removing this line because I am answers_list access elements individualy using for loop. #.summary() print only summary.
    for element in answerd_list: 
        #print(element[1].show()) #.show() was showing details information about each packets. # element is a variable if you are choosing any name.
        # scapy sending packets and answerd packets. sending packets was 0 and receiving or answers packet was 1 in lists.
        print(element[1].psrc) # printing the client ip
        print(element[1].hesrc) # printing the hardware source 
        print("----------------------------------------------------") # this is a more redaiable.
        
scan("192.169.62.2/24")   
    