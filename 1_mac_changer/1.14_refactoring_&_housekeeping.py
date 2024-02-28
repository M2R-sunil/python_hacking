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
def check_current_mac(interface):
    ifconfig_output = subprocess.check_output(["ifconfig", interface]) # .check_output this module check output in terminal.
    ifconfig_read_output = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output) # this is capture the mac address in the output.
    if ifconfig_read_output: # this is handling error in terminal.
         return ifconfig_read_output.group(0)
    else:
         print("[-] plese enter the right result]"])    
    
       
 current_mac = check_current_mac(options.interface) # this is capture the check_current_mac function 
 print("current mac = " + str(current_mac))  # str(current_mac) this is using casting in python. this is treating a variable in string for str.
 options = get_arguments() 
 






