#!/usr/bin/env python

import subprocess
import optparse 
import re # this is important regular expressions.
def get_arguments(): 
    parser = parser.Option.Parser() 
    parser.add_option("-i", "--interface", dest="interface", help="this is showing interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="this is showing interface")
    (options, arguments) = parser.add_args() 
    if not options.interface: 
        parser.error("[-] plese enter the interface")
    elif not options.new_mac: 
        parser.error("[-] plese enter the new mac address")    
    return options
def change_mac(interface, new_mac): 
    print("change a mac " + interface + "to" + new_mac)
    subprocess call(["ifconfig", interface, "down"]) 
    subprocess call(["ifconfig", interface, "hw", "ether", "down"])   
    subprocess call(["ifconfig", interface, "up"]) 
    
 options = get_arguments() 


ifconfig_output = subprocess.check_output(["ifconfig", options.interface]) # .check_output this module check output in terminal.
print(ifconfig_output)
ifconfig_read_output = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output) # this is capture the mac address in the output.
if ifconfig_read_output: # this is handling error in terminal.
    print(ifconfig_read_output.group(0)) 
else:
    print("[-] plese enter the right result]"])    
    



