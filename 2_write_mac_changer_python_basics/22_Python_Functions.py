#!/usr/bin/env python2

import subprocess
import optparse

def change_mac_payload(interface, new_mac):
    print("[+] Changing Mac address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    subprocess.call(["ifconfig", interface, "up"])

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
(options, arguments) = parser.parse_args()

change_mac_payload(options.interface, options.new_mac)

# -i wlan0 -m 99:88:99:55:88:00
