#!/usr/bin/env python

import subprocess
import optparse 
def get_arguments(): # this function capture the values in the user.
    parser = parser.Option.Parser() 
    parser.add_option("-i", "--interface", dest="interface", help="this is showing interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="this is showing interface")
    return parser.add_args() 
    
def change_mac(interface, new_mac): 
    print("change a mac " + interface + "to" + new_mac)
    subprocess call(["ifconfig", interface, "down"]) 
    subprocess call(["ifconfig", interface, "hw", "ether", "down"])   
    subprocess call(["ifconfig", interface, "up"]) 
    
(options, arguments) = get_arguments() # this is capture the parser.add_args()    
change_mac(options.interface, options.new_mac)
