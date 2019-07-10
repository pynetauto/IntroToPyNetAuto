# Source code 5.5 - telnet5multi.py

#!/usr/bin/env python3.6

import getpass
import telnetlib

user = input("Enter your username: ")
password = getpass.getpass()

#Read 'for ~ n range' function to read continuous number range 101-103 and use as HOST IP
for n in range (101, 104):
    HOST = ("192.168.229." + str(n))
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

#configure VLAN 2-10 with names using 'for ~ in range' loop
    tn.write(b"conf t\n")

    for n in range (2, 11):
        tn.write(b"vlan " + str(n).encode('UTF-8') + b"\n")
        tn.write(b"name LAB5_VLAN_" + str(n).encode('UTF-8') + b"\n")

    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))