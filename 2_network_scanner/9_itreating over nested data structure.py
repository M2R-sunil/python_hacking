#!/usr/bin/env python

import scapy.all as scapy

def scan(ip): # this is a define a scapy function
    arp_request = scapy.ARP(pdst=ip) # scapy.ARP() this is print the summary this is a scapy function # this is a module for scapy. #(pdst=ip) this is second mathod printing the ip address.
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff::ff") # this is a module for scapy for mac address destination to broadcast mac scapy.Ether() # this is set to  destination to broadcast mac.
    arp_request_broadcast = broadcast/arp_request # this is / forward slash combine print the packets value. 
    answerd_list = scapy.srp(arp_request_broadcast,timeout=1, verbose=false)[0] # verbose false unused data is not printing. for better output.
  
    
    client_list = []  # creating a big list of outside of loop.
    for element in answerd_list: 
        client_dict = {"ip" :element[1].psrc, "mac" :element[1].hwsrc} # This is create a dictionary.
        client_list.append(client_dict) #this is add client dict to client_list. .append() adding the elements in client_list
         
    return (client_list)
def print_result(result_result):
        
    print("ip \t\t\t mac address \n -------------") # this is print the line after 3 tab ip to mac address and \n option is print the next line..
    for client in result_list:
       # print(client). ## this is print client list
       print(client["ip"] + "\t\t" + client["mac"]) # this is print the ip and mac in dictionary.
scan_result = scan("192.169.62.2/24")
print_result(scan_result)   
    