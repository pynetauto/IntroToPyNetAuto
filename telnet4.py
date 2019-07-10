# Source code 5.4 - telnet4.py

#!/usr/bin/env python3.6

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

#configure 100 VLANs with names using 'for ~ in range' loop
tn.write(b"conf t\n")

for n in range (2, 102):
    tn.write(b"vlan " + str(n).encode('UTF-8') + b"\n")
        tn.write(b"name PYTHON_VLAN_" + str(n).encode('UTF-8') + b"\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))