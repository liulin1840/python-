# -*- coding:utf-8 -*-
__author__ = 'liulin'

import pika
import uuid,time#uuid生成的随机字符串

class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        #只要一收到消息就调用on_response
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)
    #触发的函数,生产者发了个命令给消费者,消费者不想阻塞,
    #用于确认的,收到又返回,对上了,确保命令是我想要的结果,
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())#
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        # 先做判断? 发个服务器uuid
        while self.response is None:
            self.connection.process_data_events()
            print('no message')
            time.sleep(0.5)
        return int(self.response)
#不阻塞版的start_consumer
fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(6)
print(" [.] Got %r" % response)