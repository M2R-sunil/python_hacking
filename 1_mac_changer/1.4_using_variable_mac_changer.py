#!/usr/bin/env python

import subprocess

interface = "eth0" # this is a set a verible. interface store the "eth0" value.
new_mac = "00:11:22:33:44:55"

print("change a mac " + interface + "to" + new_mac)

subprocess.call("ifconfig "+ interface +" down", shell=True) # subprocess.call running the system coomands. and shell=True helping the running shell coomands.
subprocess.call("ifconfig" + interface + "hw ether", + new_mac, shell=True) 
subprocess.call("ifconfig" + interface + "up", shell=True) 

    