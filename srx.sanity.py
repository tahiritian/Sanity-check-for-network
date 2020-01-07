from netmiko import ConnectHandler, SSHDetect, Netmiko
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException
import re
import getpass
import os

output = raw_input("Please enter if precheck or postcheck is being performed:")
loginname = raw_input("Enter the username:")
name = raw_input("Enter the SRX firewall name:")
commandsfile = open("srxcommands.txt" , "r")
bastion = {  'device_type' : 'juniper_junos', 'host': name , 'username' : loginname , 'password': getpass.getpass() , 'blocking_timeout': 8 }
net_connect = ConnectHandler(**bastion)
for cmd in commandsfile:
    filename = bastion.get('host')
    filename = filename + "_" + str(output)
    with open(filename, "a") as fd:
       fd.write(repr(cmd))
       fd.write(net_connect.send_command(cmd, delay_factor=10))
net_connect.disconnect()
