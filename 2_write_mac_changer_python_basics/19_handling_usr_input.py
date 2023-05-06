#!usr/bin/env python2

import subprocess

interface = raw_input("interface > ")
new_mac = raw_input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
# this is a list method program he is a highly secure program in python
# list store the single value
# this program is working



