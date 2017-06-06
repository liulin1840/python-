# -*- coding:utf-8 -*-
__author__ = "Alex Li"
import threading,time
import queue

q = queue.Queue(maxsize=10)
#生产者就是向队列中放骨头,
def Producer(name):
    count = 1
    while True:
        q.put("骨头%s" % count)
        print("生产了骨头",count)
        count +=1
        time.sleep(0.1)


#消费者就是从队列面拿数据,
def  Consumer(name):
    #while q.qsize()>0:
    while True:
        print("[%s] 取到[%s] 并且吃了它..." %(name, q.get()))
        time.sleep(1)


#多个线程的问题,都去取数据
p = threading.Thread(target=Producer,args=("Alex",))
c = threading.Thread(target=Consumer,args=("ChengRonghua",))
c1 = threading.Thread(target=Consumer,args=("王森",))

#线程就是创建后再启动
p.start()
c.start()
c1.start()
