#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface change the mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()

def change_mac(interface, new_mac):
    print("[+] changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)

# -i eth0 -m 33:88:88:66:66:88
# this code is working return values in the functions

