#!/usr/bin/env python

import subprocess
import optparse # this is a str library of python parse the arguments of the user.

parser = optparse.OptionParser() # Option.Parser this is hold the all values for user give. #parser is a another verable.
parser.add_option("-i", "--interface", dest="interface", help="this is showing interface")
parser.add_option("-m", "--mac", dest="new_mac", help="this is showing interface")
(options, arguments) = parser.add_args() # .add_args this is a mathod, and options,arguments are variable., this program not using arguments only using the options.
# options variable contains values ex. eth0 and 00:11:22:33:44:55


interface = options.interface 
new_mac = options.new_mac 

print("change a mac " + interface + "to" + new_mac)
subprocess call(["ifconfig", interface, "down"]) # this is using for lists lists are store only one word and enclose the square brackets.
subprocess call(["ifconfig", interface, "hw", "ether", "down"])   
subprocess call(["ifconfig", interface, "up"])
    
