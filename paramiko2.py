# Source code 5.10- paramiko2.py

#[root@localhost ~]# cat paramiko2.py
#!/usr/bin/env python3.6

import paramiko
import time
from datetime import datetime
t_ref = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

file1 = open("routerlist")

for line in file1:
    print(t_ref)
    print ("Now logging into " + (line))
    ip_address = line.strip()

    file2= open("adminpass")
    for line1 in file2:
        username = line1.strip()
        for line2 in file2:
            password = line2.strip()

            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=ip_address,username=username,password=password)
            print ("Successful connection to " + (ip_address) +"\n")
            print ("Now completing following tasks : " + "\n")

            remote_connection = ssh_client.invoke_shell()
            remote_connection.send("configure terminal\n")
            print ("Configuring NTP Server")
            remote_connection.send("ntp server 192.168.229.133\n")
            remote_connection.send("end\n")
            remote_connection.send("copy running-config start-config\n")
            print ()

            time.sleep(2)
            output = remote_connection.recv(65535)
            print((output).decode('ascii'))

            print (("Successfully configured your device & Disconnecting from ") + (ip_address))

            ssh_client.close
            time.sleep(2)

file1.close()
file2.close()
