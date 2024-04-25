#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy


def set_load(packet, load): ## this is a refactoring the code.
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.IP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print("request")
            print(scapy_packet.show())
            
            
        elif scapy_packet[scapy.TCP].sport == 80:
            print("response")
            print(scapy_packet.show())
            

            

    packet.accept()

queue = netfilterqueue.NetfilterQueue
queue.bind(0, process_packet)
queue.run()