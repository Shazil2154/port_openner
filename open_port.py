#!/usr/bin/env python

import subprocess
from sys import platform
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-p", "--port", dest="port", help='port to open or close')
    parser.add_option("-a", "--action", dest="action", help='action wether to open or close the port')
    (options, arguments) = parser.parse_args()
    if not options.port:
        parser.error('[-] Please specify a Port, use --help for more info.')
    elif not options.action:
        parser.error('[-] Please enter the action, use --help for more info.')
    return options


def change_status(port, action):
    if platform == 'win32':
        if action == 'open':
            subprocess.call('netsh advfirewall firewall add rule name="TCP Port ' +str(port)+'"'+' dir=in action=allow protocol=TCP localport='+ str(port), shell=True)
            # print('Port 8080 Opened')
            print('[+] Do not forget to close the port later or thing could get ugly😶')
        elif action == 'close':
            subprocess.call('netsh advfirewall firewall delete rule name="TCP Port ' +str(port)+'"'+' protocol=TCP localport='+str(port), shell=True)
            print('[+] Port '+str(port)+' Closed')
        else :
            print('[-] Please Select close or open')
    elif platform == 'darwin':
        print('[-] This script does not support darwin/MacOS yet')
    elif platform == 'linux' or platform == 'linux2':
        print('[-] This script does not support linux yet')


print('[+] This Script is coded By Shazil Sattar')
option = get_arguments()
change_status(option.port, option.action)
