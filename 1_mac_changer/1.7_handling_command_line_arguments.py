#!/usr/bin/env python

import subprocess
import optparse # this is a str library of python parse the arguments of the user.

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="this is interface")
parser.parse_args()


interface = raw_input("interface >") # input function get the input for user
new_mac = raw_input("new_mac >") # input working in python 3 and raw_input working python2.

print("change a mac " + interface + "to" + new_mac)
subprocess call(["ifconfig", interface, "down"]) # this is using for lists lists are store only one word and enclose the square brackets.
subprocess call(["ifconfig", interface, "hw", "ether", "down"])   
subprocess call(["ifconfig", interface, "up"])
    
