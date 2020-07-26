#! /usr/bin/env python3

import optparse
import subprocess

def get_inputs():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Specify the Interface")
    parser.add_option("-m","--newmac",dest="newMAC",help="provide new mac for the selected interface")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-]Please select the interface, OR , use help for more info")
    if not options.newMAC:
        parser.error("[-] Please specify new mac or use help for more info")
    if (options.newMAC) != "None":
        change_MAC(options.interface, options.newMAC)
        print("Your MAC address changed successfully!")
        return options

def change_MAC(interface,newMAC):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",newMAC])
    subprocess.call(["ifconfig",interface , "up"])

options = get_inputs()









