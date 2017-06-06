# -*- coding:utf-8 -*-
__author__ = 'liulin'

import pika
import sys
#收音机效果
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

#message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message ="hello"
channel.basic_publish(exchange='logs',#转发器
                      routing_key='',#写key名
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
#这个程序就是个广播,三个客户端都会接受到发送的消息