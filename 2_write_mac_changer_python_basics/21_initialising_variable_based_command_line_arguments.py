#!/usr/bin/env python2

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")
parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac
print("[+] changing MAC address for " + interface + " to " + new_mac)
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


# python mac_changer.py -i wlan0 -m 22:44:88:44:33:33
# this coomand run the terminal