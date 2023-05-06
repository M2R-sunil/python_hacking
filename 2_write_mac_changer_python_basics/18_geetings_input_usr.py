#!/usr/bin/env python2

import subprocess

interface = raw_input("interface > ")
new_mac = raw_input("new MAC > ")

print(["[+] Changing MAC address for " + interface + " to " + new_mac])

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
# this code is actually working for the python2
# python3 is  a more buggy

