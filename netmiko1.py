# Source code 5.12 - netmiko1.py

#!/usr/bin/env python3

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.229.233',
    'username': 'autoadmin',
    'password': 'cisco123',
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print (output)

config_commands = ['int loop 0', 'ip address 40.3.3.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)

for n in range (2,31):
    print ("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name LAB9_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print (output)