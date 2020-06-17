#-*- coding: utf-8 -*-
#!/usr/bin/python
import paramiko
import threading

def ssh2(ip,username,passwd,command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for cmd in command:
            stdin, stdout, stderr = ssh.exec_command(cmd)
#           #stdin.write("Y")   #简单交互，输入 ‘Y’
            output = stdout.readlines()
            #output to screen
            for o in output:
                print(o),
        print('%s\tOK\n'%(ip))
        ssh.close()
    except :
        print('%s\tError\n'%(ip))


if __name__=='__main__':
    ip_tmp = '106.13.126.'
    my_hosts = ['1', '2', '3', '4', '5', '6']
    command = ['cal','echo hello!']
    username = ""  #ssh user
    passwd = ""    #ssh passwd
    threads = []   #threadpool
    print("Begin......")
    for host in my_hosts:
        ip = ip_tmp+host
        a=threading.Thread(target=ssh2,args=(ip,username,passwd,command))
        a.start()