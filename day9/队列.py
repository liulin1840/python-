# -*- coding:utf-8 -*-
__author__ = "Alex Li"

import queue
#python 2 里面是大写的Queue
q = queue.PriorityQueue(maxsize=5)#队列中最大5个元素
#参数是个元组
q.put((-1,"chenronghua"))
q.put((3,"hanyang"))
q.put((10,"alex"))
q.put((6,"wangsen"))# 这里设置了个优先级,从小到大的出来

print(q.get())
print(q.get())
print(q.get())
print(q.get())

#卖水果,后入先出
q1  = queue.LifoQueue()

q1.put(1)
q1.put(2)
q1.put(3)
print(q1.get())
print(q1.get())
print(q1.get())

