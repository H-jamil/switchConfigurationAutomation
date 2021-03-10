# @Author: jamil
# @Date:   2021-03-10T14:22:29-06:00
# @Last modified by:   jamil
# @Last modified time: 2021-03-10T14:25:54-06:00



import paramiko
import time
import getpass
import os
from host_file import network_devices
from config_file import host_conf


UN = input("Username : ")
PW = getpass.getpass("Password : ")


# For loop allows you to specify number of hosts
for ip in  network_devices:
    print (ip)
    twrssh = paramiko.SSHClient()
    twrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    twrssh.connect(ip, port=22, username=UN, password=PW)
    remote = twrssh.invoke_shell()
    remote.send('term len 0\n')
    time.sleep(1)
    #This for loop allows you to specify number of commands  you want to enter
    #Dependent on the output of the commands you may want to tweak sleep time.
    for command in host_conf:
        remote.send(' %s \n' % command)
        time.sleep(2)
        buf = remote.recv(65000)
        print (buf)
        f = open('sshlogfile0001.txt', 'a')
        f.write(buf)
        f.close()
    twrssh.close()
