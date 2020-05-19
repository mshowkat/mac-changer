#!this is a mach changer program for changing your device mac adresses.

import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 08:00:27:1f:30:75", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
subprocess.call("ifconfig", shell=True)