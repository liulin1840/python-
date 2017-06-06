# -*- coding:utf-8 -*-
__author__ = "Alex Li"
import hashlib
import socket ,os,time
server = socket.socket()
server.bind(('0.0.0.0',9999) )
server.listen(10)
while True:
    conn, addr = server.accept()
    print("new conn:",addr)
    while True:
        print(u"等待新指令")
        data = conn.recv(1024)
        if not data:
            print(u"客户端已断开")
            break
        cmd,filename = data.decode().split()
        print(filename)


       # print(conn.recv(1024))
        if os.path.isfile(filename):
           f = open(filename,"rb")
           m = hashlib.md5()
           file_size = os.stat(filename).st_size
           conn.send( str(file_size).encode() ) #send file size
           print(conn.recv(1024).decode()) #wait for ack
           for line in f:
              m.update(line)
              conn.send(line)
           print("file md5", m.hexdigest())
           f.close()
           conn.send(m.hexdigest().encode()) #send md5
        print("send done")

server.close()
