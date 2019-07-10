# Source code 5.11 - paramiko3.py

#[root@localhost ~]# cat paramiko3.py
#!/usr/bin/env python3.6

import paramiko
import time
from datetime import datetime
t_ref = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

tftp_IP = "192.168.229.133"

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
            print ("Now making a pre-change running-config backup of " + (ip_address) + "\n")
            remote_connection = ssh_client.invoke_shell()
            remote_connection.send("copy running-config tftp\n")
            remote_connection.send((tftp_IP)+ "\n")
            remote_connection.send((ip_address)+ ".bak@" + (t_ref)+ "\n")
            time.sleep(10)
            remote_connection.send("\n")

            time.sleep(10)
            print ("Now completing the following task(s):" + "\n")
            print ("Configuring NTP Server" + "\n")
            remote_connection.send("configure terminal\n")
            remote_connection.send("no ntp server 192.168.229.133\n")
            remote_connection.send("ntp server 192.168.111.222\n")
            remote_connection.send("end\n")
            remote_connection.send("copy running-config start-config\n")
            print ()

            time.sleep(10)
            output = remote_connection.recv(65535)
            print((output).decode('ascii'))

            print (("Successfully configured your device & Disconnecting from ") + (ip_address) + "\n")
            print ("=====================================================")
#            remote_connection.send("\n")

            ssh_client.close
            time.sleep(2)

file1.close()
file2.close()