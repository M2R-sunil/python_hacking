#!/usr/bin/env python

import subprocess

interface = raw_input("interface >") # input function get the input for user
new_mac = raw_input("new_mac >") # input working in python 3 and raw_input working python2.

print("change a mac " + interface + "to" + new_mac)

#subprocess.call("ifconfig "+ interface +" down", shell=True) # subprocess.call running the system coomands. and shell=True helping the running shell coomands.
#subprocess.call("ifconfig" + interface + "hw ether", + new_mac, shell=True) 
#subprocess.call("ifconfig" + interface + "up", shell=True)  # this is unsecured command and methods ex eth0;mac // This is executed the another commands.

subprocess call(["ifconfig", interface, "down"]) # this is using for lists lists are store only one word and enclose the square brackets.
subprocess call(["ifconfig", interface, "hw", "ether", "down"])   
subprocess call(["ifconfig", interface, "up"])
