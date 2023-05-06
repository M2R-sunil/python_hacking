#!/usr/bin/env python2

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to the change the mac address")
parser.parse_args()

interface = raw_input("interface > ")
new_mac = raw_input("new MAC > ")
print("[+] Changing Mac address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
# this program showing the helping messange on the user

