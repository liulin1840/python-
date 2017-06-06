# -*- coding:utf-8 -*-
__author__ = "Alex Li"
#客户端
import socket

client = socket.socket()           #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969)) #就像当于创造了个插头,然后连接上去就可以了
while True:
    msg = raw_input(">>:").strip()
    if len(msg) == 0:continue
    client.send(msg.encode("utf-8")) #连接上去就可以看电视了
    data = client.recv(10240)
    print("recv:",data.decode())

client.close()
