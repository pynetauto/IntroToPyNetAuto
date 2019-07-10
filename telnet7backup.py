# Source code 5.8 - telnet7backup.py

#!/usr/bin/env python3.6

import getpass
import telnetlib
from datetime import datetime

s = datetime.now().strftime("%Y%m%d_%H%M%S")

#Asks for username and password
user = input("Enter your username: ")
password = getpass.getpass()

#opens file called 'switchlist' and read information
f = open("switchlist")

#Telnets into Devices & gets the running-config
for line in f:
    print ("Getting running-config from " + (line))
    HOST = line.strip()
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

#Makes Term length to 0, run shows commands & reads all output,
#then saves files with time stamp
    tn.write(("terminal length 0\n").encode('ascii'))
    tn.write(("show ver | in uptime\n").encode('ascii'))
    tn.write(("show vlan\n").encode('ascii'))
    tn.write(("show running-config\n").encode('ascii'))
    tn.write(("exit\n").encode('ascii'))
    readoutput = tn.read_all()
    saveoutput = open(str(s) + "_running_config_" + HOST, "wb")
    saveoutput.write(readoutput)
    saveoutput.close
