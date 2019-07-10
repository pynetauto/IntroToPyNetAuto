# Source code 5.7 - telnet6multi.py

#!/usr/bin/env python3.6

import getpass
import telnetlib

user = input("Enter your username: ")
password = getpass.getpass()

#opens file called 'switchlist' and read information
f = open("switchlist")

#uses 'f' from 'switchlist' and uses to telnet into Cisco devices
for line in f:
    print ("Configuring Switch " + (line))
    HOST = (line)
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

#configures VLAN 2-30 with names using 'for ~ in range' loop
    tn.write(b"conf t\n")

    for n in range (2, 31):
        tn.write(b"vlan " + str(n).encode('UTF-8') + b"\n")
        tn.write(b"name LAB6_VLAN_" + str(n).encode('UTF-8') + b"\n")

    tn.write(b"end\n")
    tn.write(b"write memory\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
