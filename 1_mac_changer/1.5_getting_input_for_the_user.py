#!/usr/bin/env python

import subprocess

interface = raw_input("interface >") # input function get the input for user
new_mac = raw_input("new_mac >") # input working in python 3 and raw_input working python2.

print("change a mac " + interface + "to" + new_mac)

subprocess.call("ifconfig "+ interface +" down", shell=True) # subprocess.call running the system coomands. and shell=True helping the running shell coomands.
subprocess.call("ifconfig" + interface + "hw ether", + new_mac, shell=True) 
subprocess.call("ifconfig" + interface + "up", shell=True) 

    