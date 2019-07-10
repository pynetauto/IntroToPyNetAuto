# Source code for cron lab - paramiko4_cpu_mon.py

#!/usr/bin/env python3.6

import paramiko
import time

file1 = open("routerlist1.txt")

for line in file1:
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
            print ("Monitoring Router's Top 5 CPU Utilization")
            remote_connection.send("show clock\n")
            remote_connection.send("show processes cpu sorted | exc 0.00\n")
            time.sleep(1)
            remote_connection.send("exit\n")
            print ()
            time.sleep(2)
            output = remote_connection.recv(65535)
            print((output).decode('ascii'))

            ssh_client.close
            time.sleep(2)

file1.close()
file2.close()
