#!/usr/bin/env python

import scapy.all as scapy

def scan(ip): # this is a define a scapy function
    arp_request = scapy.ARP(pdst=ip) # scapy.ARP() this is print the summary this is a scapy function # this is a module for scapy. #(pdst=ip) this is second mathod printing the ip address.
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff::ff") # this is a module for scapy for mac address destination to broadcast mac scapy.Ether() # this is set to  destination to broadcast mac.
    arp_request_broadcast = broadcast/arp_request # this is / forward slash combine print the packets value. 
    answerd_list = scapy.srp(arp_request_broadcast,timeout=1, verbose=false)[0] # verbose false unused data is not printing. for better output.
  
    print("ip \t\t\t mac address \n -------------") # this is print the line after 3 tab ip to mac address and \n option is print the next line..
    for element in answerd_list: 
       
        print(element[1].psrc + "\t\t" + element[1].hwsrc) # this is print output simultaneously.
        #print(element[1].hwsrc) 
        #print("----------------------------------------------------") 
        
scan("192.169.62.2/24")   
    