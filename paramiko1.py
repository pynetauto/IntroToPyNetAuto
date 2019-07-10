# Source code 5.9 - paramiko1.py

#!/usr/bin/env python3

import paramiko
import time

ip_address = "192.168.229.111"
username = "autoadmin"
password = "cisco123"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print ("Successful connection to " + (ip_address) +"\n")
print ("Now completing following tasks : " + "\n")

remote_connection = ssh_client.invoke_shell()
remote_connection.send("configure terminal\n")
print ("Adding & configuring Loopback 0")
remote_connection.send("int loop 0\n")
remote_connection.send("ip address 40.1.1.1 255.255.255.255\n")
print ("Adding & configuring Loopback 1")
remote_connection.send("int loop 1\n")
remote_connection.send("ip address 40.2.2.2 255.255.255.255\n")

for n in range (2,11):
    print (("Creating VLAN ") + str(n))
    remote_connection.send("vlan " + str(n) +  "\n")
    time.sleep(1.5)
    remote_connection.send("name LAB8_VLAN " + str(n) +  "\n")
    time.sleep(1.5)

remote_connection.send("end\n")
print ()
print (("Disconnecting from ") + (ip_address))

time.sleep(2)
output = remote_connection.recv(65535)
print((output).decode('ascii'))

ssh_client.close
