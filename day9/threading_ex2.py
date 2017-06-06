# -*- coding:utf-8 -*-
__author__ = "Alex Li"

import threading
import time
#以类的形式启动线程
class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyThread,self).__init__()
        self.n =  n
        self.sleep_time = sleep_time
    def run(self):
        print("runnint task ",self.n )
        time.sleep(self.sleep_time)
        print("task done,",self.n )


t1 = MyThread("t1",2)
t2 = MyThread("t2",4)

t1.start()
t2.start()

t1.join() #=wait()
t2.join()

print("main thread....")
