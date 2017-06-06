# -*- coding:utf-8 -*-
__author__ = "Alex Li"
import socket
client = socket.socket()

#client.connect(('192.168.16.200',9999))
client.connect(('localhost',9999))

while True:
    cmd = raw_input(">>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024) ##u接受命令结果的长度
    print(u"命令结果大小:",cmd_res_size)
    client.send(u"准备好接收了,可以发了".encode("utf-8"))
    received_size = 0
    received_data = b''
    #接收的数据与接收的大小
    cmd_size = int(cmd_res_size.decode("utf-8"))
    while received_size < int(cmd_res_size.decode("utf-8")) :
        data = client.recv(1024)
        received_size += len(data)
        #u每次收到的有可能小于1024，所以必须用len判断
        #print(data.decode())
        received_data += data
    else:
        print("cmd res receive done...",received_size)
        print(received_data.decode("utf-8"))


client.close()

