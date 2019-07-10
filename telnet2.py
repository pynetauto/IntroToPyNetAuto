# Source code 5.2 - telnet2.py

import getpass
import telnetlib

HOST = "192.168.229.101"
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

#configure 5 VLANs with VLAN names
tn.write(b"enable\n")
tn.write(b"cisco123\n")
tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name Data_vlan_2\n")
tn.write(b"vlan 3\n")
tn.write(b"name Data_vlan_3\n")
tn.write(b"vlan 4\n")
tn.write(b"name Data_vlan_4\n")
tn.write(b"vlan 5\n")
tn.write(b"name Wireless_vlan_1\n")
tn.write(b"vlan 6\n")
tn.write(b"name Voice_vlan_1\n")
tn.write(b"exit\n")

#configure gi1/0 - gi1/3 as access siwtchports and assign vlan 5 for wireless APs
tn.write(b"interface range gi1/0 - 3\n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 5\n")

#configure gi2/0 - gi2/3 as access switchports and assign vlan 2 for data and vlan 6 for voice
tn.write(b"interface range gi2/0 - 3\n")
tn.write(b"switchport mode access \n")
tn.write(b"switchport access vlan 2\n")
tn.write(b"switchport voice vlan 6\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
