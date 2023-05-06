#!usr/bin/env python2
import subprocess

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 22:44:44:36:44:33", shell=True)

subprocess.call("ifconfig wlan0 up", shell=True)



