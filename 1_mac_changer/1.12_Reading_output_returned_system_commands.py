#!/usr/bin/env python

import subprocess
import optparse 
def get_arguments(): # this function capture the values in the user.
    parser = parser.Option.Parser() 
    parser.add_option("-i", "--interface", dest="interface", help="this is showing interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="this is showing interface")
    (options, arguments) = parser.add_args() # use options and arguments variables in hare.
    if not options.interface: # if not this is condition making decisions in python.
        parser.error("[-] plese enter the interface")
    elif not options.new_mac: #elif not is condition decision making in python.
        parser.error("[-] plese enter the new mac address")    
    return options
def change_mac(interface, new_mac): 
    print("change a mac " + interface + "to" + new_mac)
    subprocess call(["ifconfig", interface, "down"]) 
    subprocess call(["ifconfig", interface, "hw", "ether", "down"])   
    subprocess call(["ifconfig", interface, "up"]) 
    
 options = get_arguments() 
#change_mac(options.interface, options.new_mac) # comment this line because captur this data in check_output

ifconfig_output = subprocess.check_output(["ifconfig", options.interface]) # .check_output this module check output in terminal.
print(ifconfig_output)

## now first step algorithm is done.


