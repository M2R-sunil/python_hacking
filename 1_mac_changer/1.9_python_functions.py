#!/usr/bin/env python

import subprocess
import optparse 
def change_mac(interface, new_mac): ## creating change_mac function. interface and new_mac create any of you want.
    print("change a mac " + interface + "to" + new_mac)
    subprocess call(["ifconfig", interface, "down"]) 
    subprocess call(["ifconfig", interface, "hw", "ether", "down"])   
    subprocess call(["ifconfig", interface, "up"]) ## this code part of change_mac function.
    
parser = optparse.Option.Parser()
parser.add_option("-i", "--interface", dest="interface", help="this is showing interface")
parser.add_option("-m", "--mac", dest="new_mac", help="this is showing interface")
(options, arguments) = parser.add_args() 

#interface = options.interface # no need of the this two lines because the using function. and use the change_mac function.
#new_mac = options.new_mac 

change_mac(options.interface, options.new_mac)
